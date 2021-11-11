import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
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

        def build_game(owned_game):
            return {
                "id": owned_game.game.id,
                "title": owned_game.game.title,
                "genre": owned_game.game.genre,
            }

        games = list(map(build_game, list(owned_games)))
        print(games)
        for game in games:
            print(game)

        return JsonResponse(games, safe=False)

        # print(games_owned)
        # for game in games_owned:
        #     print(game.game.title)
        # <QuerySet [{'id': 1, 'user_id': 1, 'game_id': 1}, {'id': 3, 'user_id': 1, 'game_id': 3}, {'id': 4, 'user_id': 1, 'game_id': 3}, {'id': 5, 'user_id': 1, 'game_id': 3}, {'id': 6, 'user_id': 1, 'game_id': 3}]>
        # games_owned is a QuerySet, and if wrap in list(), it works as expected
        # json_response = json.dumps(list(games_owned))
        serialized = serializers.serialize("json", games)
        return HttpResponse(serialized, content_type='application/json')



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
