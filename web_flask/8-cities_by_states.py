#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    display comment
    """
    return render_template("7-states_list.html", states=storage.all(State))


@app.route('/cities_by_states')
def cities_by_state():
    """
    display comment
    """
    states = []
    for key, state in storage.all("State").items():
        states.append({
            'id': state.id,
            'name': state.name,
            'cities': state.cities
        })


@app.teardown_appcontext
def teardown(error):
    """
    display comment
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
