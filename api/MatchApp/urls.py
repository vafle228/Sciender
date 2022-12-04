from django.urls import path
from MatchApp.views import UserCardListAPIView, UserMatchCreateAPIView


urlpatterns = [
    path("user_cards/", UserCardListAPIView.as_view()),
    path("create", UserMatchCreateAPIView.as_view()),
]
