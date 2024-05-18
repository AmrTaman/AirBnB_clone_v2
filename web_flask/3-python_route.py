#!/usr/bin/python3
"""
iam here
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_main():
    """
    main DIR
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    hbnb dir
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_print_c(text):
    """
    dealing with variables
    """
    new_txt = " ".join(text.split('_'))
    return "C {}".format(new_txt)


@app.route("/python/<text>", strict_slashes=False)
def hello_print_py(text="is cool"):
    """
    dealing with variables
    """
    new_txt = " ".join(text.split('_'))
    return "Python {}".format(new_txt)

@app.route()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')