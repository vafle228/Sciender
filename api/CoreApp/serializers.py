from rest_framework import serializers
from CoreApp.models import ScienceInterest, WorkLink
from AuthApp.models import ScienderUser


class ScienceInterestSerialize(serializers.ModelSerializer):
    class Meta:
        model = ScienceInterest
        fields = ("name", )


class WorkLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLink
        fields = ("link", )


class ScienderUserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScienderUser
        fields = ("image", )
