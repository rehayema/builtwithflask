from cs50 import SQL
from flask import Flask, render_template, redirect, request

app = Flask(__name__)



@app.route("/")
def index():
    db = SQL("sqlite:///lecture.db")
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else: 
        name = request.form.get("name")
        if not name:
            return render_template("apology.html", message="You must provide a name.")
        email = request.form.get("email")
        if not email:
            return render_template("apology.html", message="You must provide a valid email address.")
        db = SQL("sqlite:///lecture.db")
        db.execute("INSERT INTO registrants (name, email) VALUES(:name, :email)", name=name, email=email)
        return redirect("/")

