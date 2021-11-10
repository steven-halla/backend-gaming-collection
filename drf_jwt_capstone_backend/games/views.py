from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game
from .serializers import GameSerializer


class GameList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


