#!/usr/bin/python3
"""
AirBnB python module
"""


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    display Hello HBNB
    Returns
        str: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    display HBNB!
    Returns:
        str: HBNB!
    """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """
    display C <text>
    Returns:
        str: C <text>
    """
    return "C {}".format(text).replace("_", " ")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
