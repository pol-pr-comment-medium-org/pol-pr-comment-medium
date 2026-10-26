import hashlib
from flask import Flask

app = Flask(__name__)

def digest(value):
    return hashlib.md5(value.encode()).hexdigest()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
