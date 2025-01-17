import logging
from flask import render_template, Flask
from zenaura.server import DevServer

app = Flask(__name__, static_folder="public", template_folder="public")

DEVSERVER = DevServer(app, port=5000, debug=True)

@DEVSERVER.app.route("/<string:path>")
def root(path):
    try:
        return render_template("index.html")
    except Exception as e:
        logging.info(f"Error rendering template: {e}")
        return "An error occurred.", 500

@DEVSERVER.app.route("/")
def root2():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.info(f"Error rendering template: {e}")
        return "An error occurred.", 500

if __name__ == "__main__":
    DEVSERVER.run()
