
from django.contrib import admin
from django.urls import path , include

from noticias import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('noticias.urls')),
    path('admin/', admin.site.urls),
    path('noticias/', include('noticias.urls')),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
