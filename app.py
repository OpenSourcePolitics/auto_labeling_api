from flask import Flask, request, jsonify
from utils.config import cache, config
from utils.type_helper import get_labels
from markupsafe import escape
from pipelines.classification import classify_sequence
from utils.translations_helper import translate

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
@app.route('/classify/<type>', defaults={'lang': "EN"}, methods=["POST"])
@app.route("/classify/<type>/<lang>", methods=["POST"])
def post_classify(type, lang):
    lang = escape(lang).striptags().upper()
    type = escape(type).striptags().lower()
    labels = get_labels(type)
    old_sequence = request.get_json()["sequence"]
    sequence = translate(old_sequence, lang)
    return dict(classify_sequence(sequence, labels), **{"old_sequence": old_sequence, "lang": lang, "type": type})
