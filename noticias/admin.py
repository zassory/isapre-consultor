from django.contrib import admin
from .models import Isapre , Noticia  

# Register your models here.
class IsapreAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Isapre,IsapreAdmin)
admin.site.register(Noticia,NoticiaAdmin)
