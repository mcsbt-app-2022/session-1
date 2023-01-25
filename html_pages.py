from flask import Flask, send_from_directory


app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("html", "index.html")


@app.route("/about")
def about():
    return send_from_directory("html", "about.html")


app.run(port=8080)