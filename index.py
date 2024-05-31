from flask import Flask, send_file 
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



if __name__ == "__main__":
    ZenauraServer.hydrate_app(router, scripts=[
        '<link rel="stylesheet" href="public/gigavolt.min.css">',
        '<script src="public/highlight.min.js"></script>',  
        '<script src="public/python.min.js"></script>',
        '<script>hljs.highlightAll();</script>',
    ])
    app.run(debug=True)  # Use debug mode for automatic reloading in development
  
