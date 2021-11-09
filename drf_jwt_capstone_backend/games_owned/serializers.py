from rest_framework import serializers
from .models import User
from .models import Game
from .models import GamesOwned

class GamesOwnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesOwned
        fields = ['id', 'gameid', 'userid']

