from djoser.serializers import TokenSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from AuthApp.models import BasicUser
from djoser.conf import settings
from AuthApp.models import ScienderUser


class BasicUserPermissionSerializer(ModelSerializer):
    id = SerializerMethodField()
    
    class Meta:
        model = BasicUser
        fields = ("permission", "id", )
    
    def get_id(self, obj: BasicUser):
        return ScienderUser.objects.get(user__id=obj.id).id


class ScienderTokenSerializer(TokenSerializer):
    user = BasicUserPermissionSerializer()
    
    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("user", "auth_token", )


class ScienderUserPreviewSerializer(ModelSerializer):
    class Meta:
        model = ScienderUser
        fields = ("id", "name", "surname", "image")
