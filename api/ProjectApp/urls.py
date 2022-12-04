from django.urls import path
from ProjectApp.views import ScienderProjectRetrieveAPIView


urlpatterns = [
    path("<int:pk>/detail", ScienderProjectRetrieveAPIView.as_view()),
]
