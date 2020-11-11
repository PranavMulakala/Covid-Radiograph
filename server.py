from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/new-1")
def new1():
    return render_template("new-1.html")
@app.route("/new-2")
def new2():
    return render_template("new-2.html")
@app.route("/new-3")
def new3():
    return render_template("new-3.html")

if __name__ == "__main__":
    app.run(debug=True)
