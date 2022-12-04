from AuthApp.models import ScienderUser
from CoreApp.serializers import ScienceInterestSerialize
from MatchApp.models import PreMatch, ScienderMatch
from ProjectApp.models import ScienderProject
from ProjectApp.serializers import ScienderProjectPreviewSerializer
from rest_framework import serializers


class ScienderUserCardSerializer(serializers.ModelSerializer):
    interests   = ScienceInterestSerialize(many=True)
    status      = serializers.SerializerMethodField()
    projects    = serializers.SerializerMethodField()
    
    class Meta:
        model = ScienderUser
        fields = ("id", "name", "surname", "status", "image", "interests", "projects")
    
    def get_status(self, obj: ScienderUser) -> str:
        return obj.get_status_display()
    
    def get_projects(self, obj: ScienderUser) -> list:
        return ScienderProjectPreviewSerializer(
            ScienderProject.objects.filter(tutor=obj).union(
            ScienderProject.objects.filter(team__id=obj.id)), 
            many=True
        ).data


class ScienderMatchSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = ScienderMatch
        fields = "__all__"
    

class PreMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreMatch
        fields = "__all__"
