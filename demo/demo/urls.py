from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the demo index.")

def about(request):
    return HttpResponse("This is the about page of the demo application.")