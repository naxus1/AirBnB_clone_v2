#!/usr/bin/python3
from flask import Flask
from flask import abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/cities_by_states')
def cities_by_state():
    """
    """
    states=list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_storage(exec):
    ''' Teardown storage
    '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
