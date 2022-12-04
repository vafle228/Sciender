from rest_framework import generics
from ProjectApp.serializers import ScienderProjectSerializer
from ProjectApp.models import ScienderProject


class ScienderProjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ScienderProjectSerializer
    queryset = ScienderProject.objects.all()
