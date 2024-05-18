#!/usr/bin/python3
"""
iam here
"""

from flask import Flask
from markupsafe import escape
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_print_py(text):
    """
    dealing with variables
    """
    new_txt = " ".join(text.split('_'))
    return "Python {}".format(new_txt)


@app.route('/number/<n>', strict_slashes=False)
def intger_check(n):
  """
  checking integer
  """
  if isinstance(escape(n), int):
    return "{} is a number".format(n)
  return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')