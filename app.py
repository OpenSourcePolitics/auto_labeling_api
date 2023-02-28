from flask import Flask, request, jsonify
from utils.config import cache, config

app = Flask(__name__)
cache.init_app(app, config=config)


@cache.cached()
@app.route('/ping')
def ping():
    return {"label": "pong"}
