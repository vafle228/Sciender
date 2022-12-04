from django.urls import path
from ProfileApp.views import ScienderUserInfoRetrieveAPIView, ScienderUserProjectsRetrieveAPIView


urlpatterns = [
    path("<int:pk>/info", ScienderUserInfoRetrieveAPIView.as_view()),
    path("<int:pk>/projects", ScienderUserProjectsRetrieveAPIView.as_view()),
]
