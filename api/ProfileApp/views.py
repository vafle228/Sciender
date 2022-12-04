from rest_framework import generics
from AuthApp.models import ScienderUser
from ProfileApp.serializers import ScienderUserInfoSerializer, ScienderUserProjectsSerializer


class ScienderUserInfoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ScienderUser.objects.all()
    serializer_class =  ScienderUserInfoSerializer


class ScienderUserProjectsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ScienderUser.objects.all()
    serializer_class =  ScienderUserProjectsSerializer
