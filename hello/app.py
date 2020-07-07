from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/index")
def index():
    number = random.randint(0,1)
    return render_template("index.html", number=number, name="Emma")

@app.route("/goodbye")
def bye():
    return render_template("goodbye.html")

@app.route("/hello")
def hello():
    name = request.args.get("name").title()
    if not name:
        return '<h1 style="color:red";>You must provide a name!</h1>'
    return render_template("hello.html", name=name)



