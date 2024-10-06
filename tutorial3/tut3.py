from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# login page with POST and GET methods
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Post called {usr}</h1>"

@app.route("/Pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/Features")
def features():
    return render_template("features.html")

if __name__ == "__main__":
    app.run(debug=True)