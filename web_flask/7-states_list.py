#!/usr/bin/python3
from flask import Flask, abort, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def list_state():
    """
    Comment
    """
    states = []
    for key, state in storage.all("State").items():
        states.append({'id': state.id, 'name': state.name})
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_storage(self):
    """
    Comment
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
