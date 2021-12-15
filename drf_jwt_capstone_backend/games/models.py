from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    genre = models.CharField(max_length=30)
    image = models.CharField(max_length=1500)
    system = models.CharField(max_length=100)
    release_date = models.IntegerField()
    value = models.IntegerField()


