#!/usr/bin/python3
"""Write a script that starts a Flask web
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
