from flask import Flask, render_template

#Create a Flask Instance
app = Flask(__name__)

#Create a rout decorator
@app.route("/")

#def index():
#    return "<h1>Hello World!</h1>"

def index():
    first_name = "John"
    stuff ="This is  <strong>bold</strong> text"
    return render_template("index.html", first_name=first_name, stuff=stuff)

@app.route("/user/<name>")

def user(name):
    return render_template("user.html")

#create customer error pages

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500