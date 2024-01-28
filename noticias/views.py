from django.shortcuts import render
from django.http import HttpResponse

from . import views

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def noticias(request):
    return render(request,"noticias/noticias.html")