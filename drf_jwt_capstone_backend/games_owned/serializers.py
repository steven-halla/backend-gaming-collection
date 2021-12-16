from rest_framework import serializers

from .models import GamesOwned


class GamesOwnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = GamesOwned
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('user_id', 'game_id', 'notes', 'fixed_value')

    def create(self, validated_data):
        print('validated data')
        print(validated_data)
        # print(self.initial_data)
        # why is validated_data (as well as self.validated_data empty despite is_valid being called and returning True)
        game_owned = GamesOwned.objects.create(**self.initial_data)

        return game_owned

    def update(self, game_owned, **kwargs):
        print('game_owned data')
        print(game_owned)
        GamesOwned.save(game_owned)
        # game_owned = GamesOwned.objects.update(game_owned, kwargs)
        return game_owned

    def is_valid(self, raise_exception=False):
        super().is_valid(raise_exception)
        return True

