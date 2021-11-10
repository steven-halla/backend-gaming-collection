from django.urls import path

from .views import GamesOwned

urlpatterns = [
    path('<int:pk_game>/users/<int:pk_user>/', GamesOwned.as_view(), name='games_owned')
]