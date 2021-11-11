from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from games.serializers import GameSerializer
from .models import GamesOwned
from .serializers import GamesOwnedSerializer


class GamesOwnedList(APIView):
    def get(self, request, pk_user):
        games_owned = GamesOwned.objects.filter(user_id=pk_user)
        # serializer = GameSerializer(games_owned, many=True)
        # return Response(serializer.data)
        return Response(games_owned)


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
        pass

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        game_owned = self.get_object(pk)
        serializer = GamesOwnedSerializer(game_owned)
        game_owned.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
