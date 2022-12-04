from django.urls import path
from MatchApp.views import UserCardListAPIView


urlpatterns = [
    path("user_cards/", UserCardListAPIView.as_view()),
]
