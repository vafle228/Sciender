from django.urls import path
from AuthApp.views import ScienderUserRetrieveView


urlpatterns = [
    path("info/<int:pk>/", ScienderUserRetrieveView.as_view()),
]
