import json

from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GamesOwned
from .serializers import GamesOwnedSerializer


# TypeError: Object of type QuerySet is not JSON serializable
# return JsonResponse(games_owned, safe=False)
# we are building our own response dictionary manually
# because when we try to return games_owned as json response (see ^)
# the joined game/user weren't showing up in json)
# we are building a "simpler" object/dict that will be serialized as expected
# TODO use Serializer pattern since it handles mapping django db objects to json.
def build_owned_game_for_json_serialization(owned_game):
    return {
        "id": owned_game.id,
        "game": {
            "id": owned_game.game.id,
            "title": owned_game.game.title,
            "publisher": owned_game.game.publisher,
            "genre": owned_game.game.genre,
            "image": owned_game.game.image,
            "system": owned_game.game.system,
            "release_date": owned_game.game.release_date,
            "value": owned_game.game.value,
        },
        "notes": owned_game.notes
    }

class GamesOwnedAPI(APIView):
    permission_classes = [AllowAny]

    def get_object(self, user_id, game_id):
        game_owned = GamesOwned.objects\
                .filter(user_id=user_id, game_id=game_id) \
                .select_related()
        if len(game_owned) == 0:
            raise Http404

        return game_owned[0]

    # get single games owned record
    def get(self, request, user_id, game_id):
        game_owned = self.get_object(user_id, game_id)

        game = build_owned_game_for_json_serialization(game_owned)

        return JsonResponse(game, safe=False)

    def post(self, request, user_id, game_id):
        print("add owned game 2")
        games_owned = {
            "user_id": user_id,
            "game_id": game_id,
            "notes": "N/A"
        }
        serializer = GamesOwnedSerializer(data=games_owned)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, game_id):
        print("is delete getting called")
        game_owned = self.get_object(user_id, game_id)
        serializer = GamesOwnedSerializer(game_owned)
        print("I am delete function")
        game_owned.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, user_id, game_id):  # pk = GamesOwnedId
        game_owned = self.get_object(user_id, game_id)
        game_owned.notes = request.data['notes']

        # todo confirm game owned is not null (i.e. exists)
        serializer = GamesOwnedSerializer(game_owned)
        serializer.update(game_owned, )
        return Response(serializer.data)


class GamesOwnedList(APIView):
    def get(self, request, pk_user):
        games_owned = GamesOwned.objects \
            .filter(user_id=pk_user) \
            .select_related()

        games = list(map(build_owned_game_for_json_serialization, list(games_owned)))
        for game in games:
            print(game)

        return JsonResponse(games, safe=False)



# deprecated
class GamesOwnedAdd(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("add owned game 2")
        print(request)
        games_owned = {
            "user_id": request.data['user_id'],
            "game_id": request.data['game_id'],
            "notes": "N/A"
        }
        serializer = GamesOwnedSerializer(data=games_owned)
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
        print("is delete getting called")
        game_owned = self.get_object(pk)
        serializer = GamesOwnedSerializer(game_owned)
        print("I am delete function")
        game_owned.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):  # pk = GamesOwnedId
        # request = {
        #     "id": pk,
        #     "owner_rating": request.data['owner_rating'],
        #     "review": request.data['review'],
        # }
        game_owned = self.get_object(pk)
        game_owned.notes = request.data['notes']

        # todo confirm game owned is not null (i.e. exists)
        serializer = GamesOwnedSerializer(game_owned)
        serializer.update(game_owned, )
        return Response(serializer.data)
