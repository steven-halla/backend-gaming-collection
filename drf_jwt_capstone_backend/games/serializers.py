from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'title', 'publisher',
              'genre', 'image', 'release_date',
              'value', 'rating']