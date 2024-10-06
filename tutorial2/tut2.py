from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# the home page renders the index.html file
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

if __name__ == "__main__":
	app.run()