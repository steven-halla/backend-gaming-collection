from django.contrib.auth import get_user_model
from django.http import Http404

from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class UserList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data)


class UserView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = RegistrationSerializer(user)
        return Response(serializer.data)

