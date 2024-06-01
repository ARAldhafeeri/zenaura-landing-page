import logging
import subprocess
import time
from threading import Thread, Event
import asyncio
import contextlib
from flask import Flask, render_template
from flask_sock import Sock
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from public.routes import ClientRoutes
from public.main import router
import signal 

logging.basicConfig(level=logging.INFO)


class PausingObserver(Observer):
    def dispatch_events(self, *args, **kwargs):
        if not getattr(self, '_is_paused', False):
            super(PausingObserver, self).dispatch_events(*args, **kwargs)

    def pause(self):
        self._is_paused = True

    def resume(self):
        time.sleep(self.timeout)  # allow interim events to be queued
        self.event_queue.queue.clear()
        self._is_paused = False

    @contextlib.contextmanager
    def ignore_events(self):
        self.pause()
        yield
        self.resume()


class DevServer:
    def __init__(self, debug=True, port=5000):
        self.debug = debug
        self.port = port
        self.app = Flask(__name__, static_folder="public", template_folder="public")
        self.sock = Sock()
        self.ws_client_list = []
        self.shutdown_event = Event()
        self.observer = PausingObserver()
        self.sock.init_app(self.app)
        self.loop = asyncio.new_event_loop()

        self.setup_websocket()

    def setup_websocket(self):
        @self.sock.route("/refresh")
        def refresh(ws):
            self.ws_client_list.append(ws)
            while not self.shutdown_event.is_set():
                try:
                    ws.receive()
                    ws.sleep(1)
                    ws.send("refresh")
                except Exception as e:
                    print(f"Error in WebSocket connection: {e}")
                    break

    def send_refresh_signal(self):
        logging.info("Sending refresh signal...")
        clients = self.ws_client_list.copy()
        for client in clients:
            try:
                client.send("refresh")
            except Exception as e:
                print(f"Error sending refresh: {e}")
                self.ws_client_list.remove(client)

    def get_change_handler(self):
        DEVSERVER = self

        class ChangeHandler(FileSystemEventHandler):
            def __init__(self, server):
                super().__init__()
                self.server = server

            def on_any_event(self, event):
                try:
                    logging.info(f"File {event.src_path} has changed.")
                    logging.info("Changes are live...")
                    DEVSERVER.hydrate_and_notify()
                    logging.info("Reloading browser...")
                    DEVSERVER.send_refresh_signal()
                    logging.info("Browser reloaded.")
                except Exception as e:
                    logging.info(f"Error in ChangeHandler: {e}")

        return ChangeHandler

    def start_server(self):
        try:
            self.app.run(debug=self.debug, port=self.port, use_reloader=False)
        except Exception as e:
            logging.info(f"Error starting server: {e}")

    def hydrate_and_notify(self):
        try:
            self.observer.pause()
            logging.info("Hydrating...")
            logging.info("Pausing the observer...")
            process = subprocess.Popen("python build.py", shell=True)
            process.communicate()
            logging.info("Hydrated done...")

        finally:
            logging.info("Running the observer...")
            self.observer.resume()

    def run(self):
        path = 'public'
        ChangeHandler = self.get_change_handler()
        event_handler = ChangeHandler(self)
        self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()

        server_thread = Thread(target=self.start_server, daemon=True)
        server_thread.start()

        try:
            while not self.shutdown_event.is_set():
                time.sleep(0.1)  # Shorter sleep interval
        except KeyboardInterrupt:
            logging.info("KeyboardInterrupt received, stopping...")
        finally:
            # Faster Shutdown of Observer
            self.observer.event_queue.queue.clear()
            self.observer.stop()  
            self.observer.join()  


DEVSERVER = DevServer(port=5000, debug=True)


@DEVSERVER.app.route(ClientRoutes.counter.value)
@DEVSERVER.app.route(ClientRoutes.home.value)
def root():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.info(f"Error rendering template: {e}")
        return "An error occurred.", 500

if __name__ == "__main__":
    DEVSERVER.run()


