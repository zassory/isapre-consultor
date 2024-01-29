from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Isapre(models.Model):
    nombre = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'isapre'
        verbose_name_plural = 'isapres'

    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    
    imagen1 = models.ImageField(upload_to='noticias', null=True , blank=True)

    imagen2 = models.ImageField(upload_to='noticias', null=True , blank=True)
    imagen3 = models.ImageField(upload_to='noticias', null=True , blank=True)
    imagen4 = models.ImageField(upload_to='noticias', null=True , blank=True)
    imagen5 = models.ImageField(upload_to='noticias', null=True , blank=True)
    comentario = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    isapre = models.ForeignKey(Isapre, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='noticia'
        verbose_name_plural = 'noticias'
    
    def __str__(self):
        return self.titulo
