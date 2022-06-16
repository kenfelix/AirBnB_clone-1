#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Returns “Hello HBNB!”
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Returns HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def dispaly_c(text):
    """
    Display “C ” followed by the value of the text variable
    """
    text = text.replace('_', ' ')

    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
