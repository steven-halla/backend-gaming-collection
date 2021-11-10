from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import  GamesOwnedSerializer

# Create your views here.
from ..authentication.models import User
from ..games.models import Game


class GamesOwned(APIView):

    permission_classes = [AllowAny]
    def get(self, request):

        users = User.objects.all()
        games = Game.objects.all()
        serializer = GamesOwnedSerializer(users, games)
        return Response(serializer.data)

