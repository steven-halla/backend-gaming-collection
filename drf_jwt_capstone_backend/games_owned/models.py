from django.contrib.auth.models import User
from django.db import models

from drf_jwt_capstone_backend.games.models import Game


class GamesOwned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

