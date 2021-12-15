from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


# ********* I need a new model (game collection for users) that is a join table from users and games  ***************************


class User(AbstractUser):
    middle_name = models.CharField(max_length=20)
    favorite_game = models.CharField(max_length=500)

