from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("This is the about page of the demo application.")


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]