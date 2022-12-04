import logging

from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

POST_PATH = "posts.json"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
logging.basicConfig(filename='log.log', level=logging.INFO)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

app.run(debug=True)

