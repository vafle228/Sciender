from ProjectApp.models import ScienderProject
from rest_framework import serializers

from AuthApp.serializers import ScienderUserPreviewSerializer
from CoreApp.serializers import ScienceInterestSerialize


class ScienderProjectPreviewSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = ScienderProject
        fields = ("name", "status", "about", "id")
    
    
    def get_status(self, obj: ScienderProject) -> str:
        return obj.get_status_display()


class ScienderProjectSerializer(serializers.ModelSerializer):
    status      = serializers.SerializerMethodField()
    tutor       = ScienderUserPreviewSerializer()
    interests   = ScienceInterestSerialize(many=True)
    team        = ScienderUserPreviewSerializer(many=True)
    
    class Meta:
        model = ScienderProject
        fields = "__all__"
    
    
    def get_status(self, obj: ScienderProject) -> str:
        return obj.get_status_display()