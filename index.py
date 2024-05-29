from flask import Flask, send_file, render_template
from public.main import router
from public.routes import ClientRoutes
from zenaura.server import ZenauraServer
from zenaura.client.hydrator import HydratorCompilerAdapter

hyd = HydratorCompilerAdapter()
app = Flask(__name__,
            static_folder="public"
            )

@app.route(ClientRoutes.counter.value)
@app.route(ClientRoutes.home.value)
def root():
    return send_file('public/index.html')


if __name__ == "__main__":
    ZenauraServer.hydrate_app(router)
    app.run()