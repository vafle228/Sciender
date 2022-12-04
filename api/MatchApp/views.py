from rest_framework import generics
from django.db.models import QuerySet

from rest_framework.permissions import IsAuthenticated

from AuthApp.models import ScienderUser
from MatchApp.serializera import ScienderUserCardSerializer


class UserCardListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ScienderUserCardSerializer
    
    def get_queryset(self) -> QuerySet:
        return ScienderUser.objects.exclude(id=self.request.user.scienderuser.id)
