from django.db import models

from drf_jwt_capstone_backend.authentication.models import User
from drf_jwt_capstone_backend.games.models import Game


class GamesOwned(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE, default=None)
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None)