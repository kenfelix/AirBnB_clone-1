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


@app.routes("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Renders all states in HTML template
    sorted by name
    """
    states = storage.all('State')
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def remove_session(context):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')