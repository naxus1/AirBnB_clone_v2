#!/usr/bin/python3
"""
AirBnB
"""


from flask import Flask, abort, render_template

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
    return "C {:s}".format(text).replace("_", " ")


@app.route("/python")
@app.route("/python/<text>")
def ptythont(text="is cool"):
    """
    display python is cool
    Returns:
        str: Python <text>
    """
    return "Python {:s}".format(text).replace("_", " ")


@app.route("/number/<n>")
def number(n):
    """
    display n is a number
    Returns:
        str: n is a number
    """
    if n.isdigit() == 1:
        return "{} is a number".format(n)
    else:
        abort(404)


@app.route("/number_template/<n>")
def number_template(n):
    """
    display template
    Returns:
       str: n is a number
    """
    if n.isdigit() == 1:
        return render_template("5-number.html", n=n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
