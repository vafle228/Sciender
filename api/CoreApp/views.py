from rest_framework import generics
from CoreApp.serializers import ScienderUserImageSerializer

from rest_framework.permissions import IsAuthenticated


class ScienderUserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ScienderUserImageSerializer
    permission_classes = [IsAuthenticated, ]
    
    def get_object(self):
        return self.request.user.scienderuser
