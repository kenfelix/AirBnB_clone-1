#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from email.policy import default, strict
from flask import Flask, render_template

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
    """display “C ” followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C " + text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def pytext(text: str = "is cool"):
    """display “C ” followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "Python " + text


@app.route("/number/<n>", strict_slashes=False)
def number(n: int):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<n>", strict_slashes=False)
def num_template(n: int):
    """display “n is a number” only if n is an integer"""
    render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
