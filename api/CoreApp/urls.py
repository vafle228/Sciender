from django.urls import path
from CoreApp.views import ScienderUserRetrieveAPIView


urlpatterns = [
    path("image/", ScienderUserRetrieveAPIView.as_view()),
]
