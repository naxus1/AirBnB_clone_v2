#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/states_list')
def states_list():
    """display a HTML page with a list of states
    Returns:
        str: rendered html
    """
    return render_template("7-states_list.html", states=storage.all(State))


@app.teardown_appcontext
def teardown(exc):
    """called after each request
    Args:
        exc (Exception): unknown, seems necessary based on docu
    """
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
