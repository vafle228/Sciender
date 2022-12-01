from rest_framework import serializers
from AuthApp.models import BasicUser, ScienderUser


class BasicUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicUser
        fields = ("id", "username", "email")


class ScienderUserModelSerializer(serializers.ModelSerializer):
    user = BasicUserModelSerializer()
    
    class Meta:
        model = ScienderUser
        fields = "__all__"
