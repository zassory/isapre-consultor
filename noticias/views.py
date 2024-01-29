from django.shortcuts import render
from noticias.models import Isapre , Noticia

from . import views

# Create your views here.

def noticias(request):

    noticias = Noticia.objects.all()
    isapre = Isapre.objects.all()

    return render(request,"noticias/noticias.html",{
        "noticias":noticias,
        "isapre":isapre
    })

def noticia(request , id):

    noticia = Noticia.objects.get(id=id)
    

    return render(request, "noticia/noticia.html", {
        "noticia":noticia
    })