from rest_framework import serializers

from .models import GamesOwned


class GamesOwnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = GamesOwned
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('user_id', 'game_id')

    def create(self, validated_data):
        print('validated data')
        print(validated_data)
        # print(self.initial_data)
        # why is validated_data (as well as self.validated_data empty despite is_valid being called and returning True)
        owned_game = GamesOwned.objects.create(**self.initial_data)

        return owned_game
    #
    # def is_valid(self, raise_exception=False):
    #     return True

