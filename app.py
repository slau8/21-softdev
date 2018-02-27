from flask import Flask, render_template, request, redirect, flash, url_for
from utils import nasa

import os

app = Flask(__name__)
app.secret_key = os.urandom(128)

# Landing page; displays the home page
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("main.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
