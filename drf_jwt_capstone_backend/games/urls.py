from django.urls import path
from .views import GameList

urlpatterns = [
    path('', GameList.as_view(), name="gamelist")
]