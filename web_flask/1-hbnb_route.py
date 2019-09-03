#!/usr/bin/python3
"""
Write a script that starts a Flask web application
/hbnb: display “HBNB
"""

from flask import Flask
app = Flask(__name__)

app.url_map.strict_slashes = False

@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
