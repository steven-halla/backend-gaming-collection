from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from games_owned.views import GamesOwnedAdd
from .views import RegisterView, UserList, UserView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserList.as_view(), name="users"),
    path('users/<int:pk>/', UserView.as_view(), name="user"),
    path('games/<int:pk_game>/users/<int:pk_user>', GamesOwnedAdd.as_view(), name="gamesowned")
]
