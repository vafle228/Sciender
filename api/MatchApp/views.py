from AuthApp.models import ScienderUser
from django.db.models import QuerySet
from MatchApp.models import PreMatch, ScienderMatch
from MatchApp.serializera import (PreMatchFromSerializer, PreMatchSerializer,
                                  PreMatchToSerializer,
                                  ScienderMatchSeriazlizer,
                                  ScienderUserCardSerializer)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer


class UserCardListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ScienderUserCardSerializer
    
    def get_queryset(self) -> QuerySet:
        return ScienderUser.objects.exclude(id=self.request.user.scienderuser.id)


class UserMatchCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, *args, **kwargs):
        to_user_id = self.request.data.get("to_user")
        from_user = self.request.user.scienderuser
        to_user = ScienderUser.objects.get(id=to_user_id)
        
        if PreMatch.objects.filter(to_user=to_user, from_user=from_user).exists():
            return Response(data="Error", status=403)
        return super().post(request, *args, **kwargs)
    
    def get_serializer_class(self) -> ModelSerializer:
        to_user_id = self.request.data.get("to_user")
        
        from_user = self.request.user.scienderuser
        to_user = ScienderUser.objects.get(id=to_user_id)
        
        self.request.data["from_user"] = from_user.id
        
        if PreMatch.objects.filter(to_user=from_user, from_user=to_user).exists():
            return ScienderMatchSeriazlizer
        return PreMatchSerializer


class ToUserPreMatchListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PreMatchFromSerializer
    
    def get_queryset(self) -> QuerySet:
        return PreMatch.objects.filter(to_user=self.request.user.scienderuser)


class FromUserPreMatchListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PreMatchToSerializer
    
    def get_queryset(self) -> QuerySet:
        return PreMatch.objects.filter(from_user=self.request.user.scienderuser)


class ScienderMatchListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ScienderMatchSeriazlizer
    
    def get_queryset(self) -> QuerySet:
        user = self.request.user.scienderuser
        return ScienderMatch.objects.filter(to_user=user).union(
            ScienderMatch.objects.filter(from_user=user)
        )
