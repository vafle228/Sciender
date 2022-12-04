from AuthApp.models import ScienderUser
from ProjectApp.models import ScienderProject
from ProjectApp.serializers import ScienderProjectPreviewSerializer
from rest_framework import serializers


class ScienderUserInfoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = ScienderUser
        fields = (
            "id", "name", "surname", "work_links", 
            "about", "image", "status", "permission", "specialty", 
        )
    
    def get_status(self, obj: ScienderUser) -> str:
        return obj.get_status_display()


class ScienderUserProjectsSerializer(serializers.ModelSerializer):
    projects    = serializers.SerializerMethodField()
    status      = serializers.SerializerMethodField()
    
    class Meta:
        model = ScienderUser
        fields = ("id", "name", "surname",  "projects", "image", "status",)
    
    def get_projects(self, obj: ScienderUser) -> list:
        return ScienderProjectPreviewSerializer(
            ScienderProject.objects.filter(tutor=obj).union(
            ScienderProject.objects.filter(team__id=obj.id)), 
            many=True
        ).data
    
    def get_status(self, obj: ScienderUser) -> str:
        return obj.get_status_display()
