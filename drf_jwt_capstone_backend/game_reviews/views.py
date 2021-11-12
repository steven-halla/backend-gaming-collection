from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GameReviews
from .serializers import GameReviewsSerializer
#
# class GameReviewsHandler(APIView):
#     def get(self, request, pk_game):
#