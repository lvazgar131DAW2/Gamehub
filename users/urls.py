from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registro/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('perfil/', views.ProfileView.as_view(), name='profile'),
    path('mis-juegos/', views.MyGamesView.as_view(), name='my_games'),
    path('mis-resenas/', views.MyReviewsView.as_view(), name='my_reviews'),
]


