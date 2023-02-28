from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def predict():
    print(request.get_json())
    return {"label": "NEG"}