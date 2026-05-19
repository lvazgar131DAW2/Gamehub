from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('juegos/', include('games.urls')),
    path('resenas/', include('reviews.urls')),
    path('usuarios/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)