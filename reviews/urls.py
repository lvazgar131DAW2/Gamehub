from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('juego/<int:game_pk>/crear/', views.ReviewCreateView.as_view(), name='review_create'),
    path('resena/<int:pk>/editar/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('resena/<int:pk>/eliminar/', views.ReviewDeleteView.as_view(), name='review_delete'),
]

