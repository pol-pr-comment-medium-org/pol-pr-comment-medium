from django.http import HttpResponse
import requests

def greet(request):
    name = request.GET.get("name", "")
    return HttpResponse("<h1>Hello " + name + "</h1>")

def fetch(url):
    return requests.get(url, verify=False)
