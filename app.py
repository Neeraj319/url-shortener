import os

import dotenv
from flask import Flask, flash, redirect, render_template, request

from models import add_to_db, getFullUrl, getFullUrlByShorten

dotenv.load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create_shorten__url():
    url_from_form = request.form["url"]
    if url := getFullUrl(url=url_from_form):
        shorten_url = url
    else:
        shorten_url = add_to_db(url=url_from_form)

    flash(f"shorten url : {shorten_url}")
    return redirect("/")


@app.route("/<shorten_url>", methods=["GET"])
def redirect_to(shorten_url):
    full_url = getFullUrlByShorten(shoreten_link=shorten_url)
    return redirect(full_url.url)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
