#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route("/python", strict_slashes=False)
def display_python(text='is cool'):
    """
    Displays  “Python ”, followed by the value of the text variable
    The default value of text is “is cool”
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """
    display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page only if n is an integer
    """
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
