from django.db import models
from authentication.models import User
from games.models import Game


class GamesOwned(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)


