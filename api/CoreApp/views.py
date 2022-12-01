from rest_framework import generics
from CoreApp.serializers import ScienderUserModelSerializer
from AuthApp.models import ScienderUser

from rest_framework.permissions import IsAuthenticated


class ScienderUserRetrieveView(generics.RetrieveAPIView):
    queryset = ScienderUser.objects.all()
    serializer_class = ScienderUserModelSerializer
    permission_classes = [IsAuthenticated, ]
