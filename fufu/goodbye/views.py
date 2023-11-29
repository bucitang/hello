from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "goodbye/index.html")

def greet(request, name):
    return render(request, "goodbye/greet.html", {
        "name": name.capitalize()
    })