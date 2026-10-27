from django.http import HttpResponse

def greet(request):
    name = request.GET.get("name", "")
    return HttpResponse("<h1>Hello " + name + "</h1>")
