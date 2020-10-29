import os
from flask import Flask, flash, jsonify, url_for, redirect, render_template,request, session, send_from_directory

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/komix")
def komix():
    return render_template("komix.html")

@app.route("/drawings")
def drawings():
    return render_template("drawings.html")

@app.route("/clothing")
def clothing():
    return render_template("clothing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(app, debug=True)
