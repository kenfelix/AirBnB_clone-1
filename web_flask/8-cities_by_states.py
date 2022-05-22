#!/usr/bin/python3
"""
Must be listening on 0.0.0.0, port 5000
Must use storage for fetching data from the storage engine
Remove the current SQLAlchemy Session after each request
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.routes("/cities_by_states", strict_slashes=False)
def list_cities_by_states():
    """
    Renders states and their citires in HTML template
    sorted by name
    """
    states = storage.all('State')
    return render_template('8-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(context):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
