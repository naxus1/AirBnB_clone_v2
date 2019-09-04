#!/usr/bin/python3
"""
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    display states in html
    Returns:
        str: html with list states
    """
    return render_template("7-states_list.html", states=storage.all(State))


@app.teardown_appcontext
def teardown(exc):
    """
    display
    Args:
        exc.
    """
    storage.close()


@app.route('/cities_by_states')
def cities_by_state():
    """
    display states in html
    Returns
        str: html with list states
    """
    states = []
    for key, state in storage.all("State").items():
        states.append({
            'id': state.id,
            'name': state.name,
            'cities': state.cities
        })

    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
