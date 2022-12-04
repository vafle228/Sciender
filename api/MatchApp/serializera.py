from rest_framework import serializers
from AuthApp.models import ScienderUser
from CoreApp.serializers import ScienceInterestSerialize
from ProjectApp.serializers import ScienderProjectPreviewSerializer

from ProjectApp.models import ScienderProject


class ScienderUserCardSerializer(serializers.ModelSerializer):
    interests   = ScienceInterestSerialize(many=True)
    status      = serializers.SerializerMethodField()
    projects    = serializers.SerializerMethodField()
    
    class Meta:
        model = ScienderUser
        fields = ("name", "surname", "status", "image", "interests", "projects")
    
    def get_status(self, obj: ScienderUser) -> str:
        return obj.get_status_display()
    
    def get_projects(self, obj: ScienderUser) -> list:
        return ScienderProjectPreviewSerializer(
            ScienderProject.objects.filter(tutor=obj).union(
            ScienderProject.objects.filter(team__id=obj.id)), 
            many=True
        ).data