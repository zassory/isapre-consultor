from django.urls import path
from django.conf import settings

from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('', views.noticias, name="Noticias"),
    path('noticia/<int:id>', views.noticia , name="Noticia")
]

# urlpatterns += static(
#     settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)