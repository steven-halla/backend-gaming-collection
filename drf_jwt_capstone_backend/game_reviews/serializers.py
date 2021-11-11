from rest_framework import serializers

from .models import GameReviews

class GameReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameReviews
        fields = ('user_id', 'game_id', 'review', 'rating')

    def create(self, validated_data):
        print('validated data')
        print(validated_data)
        game_reviews = GameReviews.objects.create(**self.initial_data)

        return game_reviews


