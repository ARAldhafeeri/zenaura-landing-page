import os
import sys
import subprocess
from flask import Flask, send_file  # Use send_from_directory for serving static files
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Import routes and server logic
from public.main import router
from public.routes import ClientRoutes
from zenaura.server import ZenauraServer
from zenaura.client.dom import zenaura_dom

app = Flask(__name__, static_folder="public")  # Set the static URL path to ""

# Use send_from_directory for serving static files (including index.html)
@app.route(ClientRoutes.counter.value)
@app.route(ClientRoutes.home.value)
def root():
    return send_file('public/index.html')


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, restart_server):
        self.restart_server = restart_server

    def on_any_event(self, event):
        if not event.is_directory:  # Only restart on file changes, not directory events
            print(f"File {event.src_path} has changed, restarting server...")
            self.restart_server()


def restart_server():
    global server_process
    if server_process:
        server_process.terminate()
        server_process.wait()
    server_process = subprocess.Popen([sys.executable, __file__, 'run'])  # Pass 'run' as argument


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        ZenauraServer.hydrate_app(router, scripts=[
            '<link rel="stylesheet" href="public/gigavolt.min.css">',
            '<script src="public/highlight.min.js"></script>',   # Update the paths for scripts
            '<script src="public/python.min.js"></script>',
            '<script>hljs.highlightAll();</script>',
        ])
        app.run(debug=True)  # Use debug mode for automatic reloading in development
    else:
        server_process = None
        path = 'public'

        event_handler = ChangeHandler(restart_server)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()

        try:
            ZenauraServer.hydrate_app(router, scripts=[
                '<link rel="stylesheet" href="public/gigavolt.min.css">',
                '<script src="public/highlight.min.js"></script>',   # Update the paths for scripts
                '<script src="public/python.min.js"></script>',
                '<script>hljs.highlightAll();</script>',
            ])
            restart_server()  # Initial start
            observer.join()  # Wait for the observer to stop
        except KeyboardInterrupt:
            observer.stop()
        finally:
            if server_process:
                server_process.terminate()
