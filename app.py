from flask import Flask, request, jsonify
from utils.config import cache, config
from transformers import pipeline

app = Flask(__name__)
cache.init_app(app, config=config)


@cache.cached()
@app.route('/ping')
def ping():
    return {"label": "pong"}


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return classifier(data["sequence"], data["labels"])
