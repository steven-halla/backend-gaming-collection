from django.urls import path

from .views import GamesOwnedAdd, GamesOwnedList, GamesOwnedDetail

urlpatterns = [
    path('', GamesOwnedAdd.as_view()),
    path('<int:pk>', GamesOwnedDetail.as_view()),
    path('user/<int:pk_user>/', GamesOwnedList.as_view()),
]