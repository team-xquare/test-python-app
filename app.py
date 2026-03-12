from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = "4.0.0-realtest"

@app.route("/")
def index():
    return jsonify({
        "message": "Hello from xquare test app!",
        "env": os.environ.get("APP_ENV", "development"),
        "version": os.environ.get("APP_VERSION", VERSION),
        "new_feature": "added in v2",
        "v3_feature": "deploy --watch test", "v4_feature": "non-admin user test",
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": VERSION})

@app.route("/echo/<text>")
def echo(text):
    return jsonify({"echo": text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
