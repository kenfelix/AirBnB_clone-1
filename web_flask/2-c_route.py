#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from email.policy import strict
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text: str):
    """isplay “C ” followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
