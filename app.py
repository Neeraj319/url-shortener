from flask import Flask, redirect

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
