from flask import Flask, request, jsonify
from utils.config import cache, config
from utils.type_helper import get_labels
from markupsafe import escape
from pipelines.classification import classify

app = Flask(__name__)
cache.init_app(app, config=config)


@cache.cached()
@app.route('/ping')
def ping():
    return {"message": "pong"}


@cache.cached()
@app.route("/classify/<type>", methods=["POST"])
def predict(type):
    labels = get_labels(escape(type).striptags())
    data = request.get_json()
    return classify(data["sequence"], labels)
