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


@app.routes("/states", strict_slashes=False)
def states():
    """
    Renders all states in HTML template
    sorted by name
    """
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.routes("/states/<id>", strict_slashes=False)
def state_by_id(id):
    """
    Finds a state using its id
    """
    states = storage.all("State").values()
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def remove_session(context):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
