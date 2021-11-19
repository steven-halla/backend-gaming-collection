from django.urls import path

from .views import GamesOwnedAdd, GamesOwnedList, GamesOwnedDetail, GamesOwnedAPI

urlpatterns = [
    # path('', GamesOwnedAdd.as_view()),
    # path('<int:pk>/', GamesOwnedDetail.as_view()),
    path('users/<int:pk_user>/', GamesOwnedList.as_view()),

    path('users/<int:user_id>/games/<int:game_id>/', GamesOwnedAPI.as_view()),
]
