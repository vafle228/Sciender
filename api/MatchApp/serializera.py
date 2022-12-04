from AuthApp.models import ScienderUser
from CoreApp.serializers import ScienceInterestSerialize
from MatchApp.models import PreMatch, ScienderMatch
from ProjectApp.models import ScienderProject
from ProjectApp.serializers import ScienderProjectPreviewSerializer
from rest_framework import serializers
from AuthApp.serializers import ScienderUserPreviewSerializer


class ScienderUserCardSerializer(serializers.ModelSerializer):
    interests   = ScienceInterestSerialize(many=True)
    status      = serializers.SerializerMethodField()
    projects    = serializers.SerializerMethodField()
    
    class Meta:
        model = ScienderUser
        fields = ("id", "name", "surname", "status", "image", "interests", "projects", "permission")
    
    def get_status(self, obj: ScienderUser) -> str:
        return obj.get_status_display()
    
    def get_projects(self, obj: ScienderUser) -> list:
        return ScienderProjectPreviewSerializer(
            ScienderProject.objects.filter(tutor=obj).union(
            ScienderProject.objects.filter(team__id=obj.id)), 
            many=True
        ).data


class ScienderMatchSeriazlizer(serializers.ModelSerializer):
    to_user = ScienderUserPreviewSerializer()
    from_user = ScienderUserPreviewSerializer()
    
    class Meta:
        model = ScienderMatch
        fields = "__all__"
    

class PreMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreMatch
        fields = "__all__"


class PreMatchToSerializer(serializers.ModelSerializer):
    to_user = ScienderUserPreviewSerializer()
    
    class Meta:
        model = PreMatch
        fields = ("to_user", )


class PreMatchFromSerializer(serializers.ModelSerializer):
    from_user = ScienderUserPreviewSerializer()
    
    class Meta:
        model = PreMatch
        fields = ("from_user", )