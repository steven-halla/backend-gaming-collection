from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Game
from rest_framework import serializers
# from .serializer import GameSerializer
from django.contrib.auth.models import User

from .serializers import GameSerializer


class GameList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        games = Game.objects.all();
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
