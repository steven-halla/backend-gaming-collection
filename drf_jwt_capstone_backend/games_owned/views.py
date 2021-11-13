from django.core import serializers
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GamesOwned
from .serializers import GamesOwnedSerializer


class GamesOwnedList(APIView):
    def get(self, request, pk_user):
        owned_games = GamesOwned.objects\
            .filter(user_id=pk_user) \
            .select_related()

        def build_owned_game(owned_game):
            return {
                "id": owned_game.id,
                "game": {
                    "id": owned_game.game.id,
                    "title": owned_game.game.title,
                    "publisher": owned_game.game.publisher,
                    "genre": owned_game.game.genre,
                    "image": owned_game.game.image,
                    "release_data": owned_game.game.release_date,
                    "value": owned_game.game.value,
                    "rating": owned_game.game.rating,

                }
            }

        games = list(map(build_owned_game, list(owned_games)))
        for game in games:
            print(game)

        return JsonResponse(games, safe=False)


class GamesOwnedAdd(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("add owned game")
        print(request)
        serializer = GamesOwnedSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GamesOwnedDetail(APIView):

    def get_object(self, pk):
        try:
            return GamesOwned.objects.get(pk=pk)
        except GamesOwned.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        print("i am get function")
        games_owned = self.get_object(pk)
        serializer = GamesOwnedSerializer(games_owned)
        return Response(serializer.data)

    def delete(self, request, pk):
        ("is delete getting called")
        game_owned = self.get_object(pk)
        serializer = GamesOwnedSerializer(game_owned)
        print("I am delete function")
        game_owned.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
