#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def mainRoute():
    """ Display: Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display: HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ Display: C + text """
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Display: Python + text or is cool """
    """ if text is None:
        return "Python is cool" """
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def isanumber(n):
    """ Display: n is a number only if n is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberstemplate(n):
    """ /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numbersoddoreven(n):
    """ /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY """
    if n % 2 == 0:
        typenum = "even"
    else:
        typenum = "odd"
    return render_template("6-number_odd_or_even.html", n=n, typenum=typenum)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
