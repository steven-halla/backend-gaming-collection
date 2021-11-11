from django.db import models
from authentication.models import User
from games.models import Game

class GameReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

