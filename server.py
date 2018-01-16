from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import os

cwd = os.getcwd()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/buy")
def buy():
    return render_template("buy.html")

@app.route("/need")
def need():
    return render_template("need.html")

@app.route("/post", methods=["POST"])
def post():
    dd = request.form['data']
    return "post succeed"

if __name__ == "__main__":
    app.run(debug=True)