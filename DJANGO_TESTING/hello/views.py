from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def seva(request):
    return HttpResponse("Hello, Seva!")

def tema(request):
    return HttpResponse("Hello, Tema!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })