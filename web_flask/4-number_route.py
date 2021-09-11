from flask import Flask
from sqlalchemy.sql.expression import text

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
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
    return  "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
