from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('juegos/', include('games.urls')),
    path('resenas/', include('reviews.urls')),
    path('usuarios/', include('users.urls')),
]