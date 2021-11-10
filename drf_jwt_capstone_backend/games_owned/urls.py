from django.urls import path

from .views import GamesOwned

urlpatterns = [
    path('', GamesOwned.as_view(), name='games_owned')
]