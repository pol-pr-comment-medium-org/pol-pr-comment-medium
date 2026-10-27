import requests
import random
import tempfile
import hashlib

def fetch(url):
    return requests.get(url, verify=False)

def password_token():
    return random.randint(0, 999999)

def write_temp():
    return tempfile.mktemp()

def digest():
    return hashlib.md5(b"password").hexdigest()
