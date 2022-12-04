from django.urls import path
from MatchApp import views


urlpatterns = [
    path("user_cards/", views.UserCardListAPIView.as_view()),
    path("create", views.UserMatchCreateAPIView.as_view()),
    
    path("", views.ScienderMatchListAPIView.as_view()),
    path("prematch/to_user", views.ToUserPreMatchListAPIView.as_view()),
    path("prematch/from_user", views.FromUserPreMatchListAPIView.as_view()),
]
