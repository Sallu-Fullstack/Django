from django.shortcuts import render, HttpResponse

# Create your views here.

def book(request):
    return HttpResponse("<h1>This is Book Shop</h2>")

def pencil(request):
    return HttpResponse("<h1>This is Pencil</h2>")