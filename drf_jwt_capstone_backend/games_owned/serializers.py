from rest_framework import serializers

from authentication.serializers import RegistrationSerializer
from games.serializers import GameSerializer
from .models import User
from .models import Game
from .models import GamesOwned

# user serializer is registerUserSerializer

class GamesOwnedSerializer(serializers.Serializer):
    users = RegistrationSerializer(many=True)
    games = GameSerializer(many=True)


