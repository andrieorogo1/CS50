from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    return render(request, "hello/index.html") # This will display the html or frontpage of the webpage

def andrie(request):
    return HttpResponse("Hello, Andrie!")

def christian(request):
    return HttpResponse("Hello, Christian!")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})


