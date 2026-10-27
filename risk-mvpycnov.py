from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    return "<h1>Hello " + name + "</h1>"

def fetch(url):
    return requests.get(url, verify=False)
