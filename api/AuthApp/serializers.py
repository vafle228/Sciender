from djoser.serializers import TokenSerializer
from rest_framework.serializers import ModelSerializer
from AuthApp.models import BasicUser
from djoser.conf import settings


class BasicUserPermissionSerializer(ModelSerializer):
    class Meta:
        model = BasicUser
        fields = ("permission", )


class ScienderTokenSerializer(TokenSerializer):
    user = BasicUserPermissionSerializer()
    
    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("user", "auth_token")
