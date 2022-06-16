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


@app.routes("/states_list", strict_slashes=False)
def list_states():
    """
    Renders states in HTML template
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(context):
    """close the database session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
