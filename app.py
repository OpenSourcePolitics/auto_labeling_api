from flask import Flask, request, jsonify
from utils.config import cache, config
from utils.type_helper import get_labels
from markupsafe import escape
from pipelines.classification import classify_sequence

app = Flask(__name__)
cache.init_app(app, config=config)


@cache.cached()
@app.route('/ping')
def ping():
    return {"message": "pong"}


@cache.cached()
@app.route("/classify/<type>", methods=["GET"])
def get_classify(type):
    labels = get_labels(escape(type).striptags())
    return {"label": labels}


@cache.cached()
@app.route("/classify/<type>", methods=["POST"])
def post_classify(type):
    labels = get_labels(escape(type).striptags())
    data = request.get_json()
    return classify_sequence(data["sequence"], labels)
