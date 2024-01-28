
from django.contrib import admin
from django.urls import path , include

from noticias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('noticias.urls')),
]
