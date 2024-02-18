#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display helo hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """display c follwed by a <text>"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """display python followed by <text>"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
