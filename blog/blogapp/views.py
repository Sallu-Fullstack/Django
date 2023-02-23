from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def itvedant(request):
    return HttpResponse("<h1>Welcome to ItVedant</h1>")