from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/greet")
def greet():
    return request.args.get("name", "")

def fetch(url):
    return requests.get(url, verify=False)
