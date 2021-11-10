from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import RegistrationSerializer
from .serializers import GamesOwnedSerializer
from django.apps import apps
# Create your views here.



class GamesOwned(APIView):

    permission_classes = [AllowAny]
    def post(self, request, pk_game, pk_user):
        User = apps.get_model('authentication.User')
        Game = apps.get_model('games.Game')

        serializer = GamesOwnedSerializer(game=pk_game, user=pk_user, many =True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

