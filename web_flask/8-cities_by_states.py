#!/usr/bin/python3
from flask import Flask
from flask import abort, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/cities_by_states')
def cities_by_state():
    list_state = list(storage.all("State").values())
    return render_template('8-cities_by_states.html', list_state=list_state)

@app.teardown_appcontext
def teardown_storage(exec):
    ''' Teardown storage
    '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
