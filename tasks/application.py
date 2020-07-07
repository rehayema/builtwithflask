from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" #save sessions on server

#activate sessions on this app which is a python dictionary
Session(app)

@app.route("/")
def tasks():
    # Checks of the current user alread has a key called todos inside his session dictionary
    # if they don't then create a key inside their sessions dictinary and set it equal to an empty list
    if "todos" not in session:
        session["todos"] = []
    return render_template("tasks.html", todos=session["todos"]) # Give task route access to the current users session todos

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        # Get whatever is stored in the html forms name attribute on the page add.html
        todo = request.form.get("task")
        #add the new todo the todos list 
        session["todos"].append(todo)
        #redirect to a route
        return redirect("/")





