from flask import Flask
from flask import Flask, redirect, url_for

app = Flask(__name__)

# decorator for the home screen
@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"

# random page called projects
@app.route("/projects")
def projects():
    return "The project page"

# accessing the admin redirecting to the home page
@app.route("/admin")
def admin():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()

