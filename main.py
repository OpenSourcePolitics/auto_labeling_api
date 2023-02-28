from flask import Flask, request

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong"}
