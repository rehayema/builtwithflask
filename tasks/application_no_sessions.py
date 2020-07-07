from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create a python list of todo notes in Global variable
todos = []

@app.route("/")
def tasks():
    return render_template("tasks.html", todos=todos) # Give task route access to todos

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        # Get whatever is stored in the html forms name attribute on the page add.html
        todo = request.form.get("task")
        #add the new todo the todos list 
        todos.append(todo)
        #redirect to a route
        return redirect("/")