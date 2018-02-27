from flask import Flask, render_template, request, flash, Markup
from utils import nasa

import os

app = Flask(__name__)
app.secret_key = os.urandom(128)

# Landing page; displays the home page
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("main.html")

@app.route("/h_mag", methods=["GET", "POST"])
def h_mag():
    h = request.args.get("h_mag")
    data = nasa.from_hmag(h)
    if data.count() == 0:
        data = []
        flash(Markup("No data found for asteroids and comets with an absolute magnitude less than <i>" + h + "</i>."))
    else:
        flash(Markup("Asteroids and comets with an absolute magnitude less than <i>" + h + "</i>:"))
    return render_template("main.html", data = data)

@app.route("/orbit_class", methods=["GET", "POST"])
def orbit_class():
    oclass = request.args.get("orbit_class")
    data = nasa.from_class(oclass)
    if data.count() == 0:
        data = []
        flash(Markup("No data found for asteroids and comets with an orbit class of <i>" + oclass + "</i>."))
    else:
        flash(Markup("Asteroids and comets with an orbit class of <i>" + oclass + "</i>:"))
    return render_template("main.html", data = data)

if __name__ == "__main__":
    nasa.main()
    app.debug = True
    app.run()
