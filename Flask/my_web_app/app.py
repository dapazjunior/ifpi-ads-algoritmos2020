from flask import Flask

app = Flask(__name__)


def home():
    return 'Hello World by Flask and Python'


if __name__ == '__main__':
    app.run(debug=True)
