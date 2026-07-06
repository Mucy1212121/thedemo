from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def about(request):
    return HttpResponse("about page")

def contact(request):
    return HttpResponse("contact page")