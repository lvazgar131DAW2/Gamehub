from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('crear/', views.GameCreateView.as_view(), name='game_create'),
    path('game/<int:pk>/editar/', views.GameUpdateView.as_view(), name='game_update'),
    path('game/<int:pk>/eliminar/', views.GameDeleteView.as_view(), name='game_delete'),
]

