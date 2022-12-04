from ProjectApp.models import ScienderProject
from rest_framework import serializers


class ScienderProjectPreviewSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = ScienderProject
        fields = ("name", "status", "about", )
    
    
    def get_status(self, obj: ScienderProject) -> str:
        return obj.get_status_display()
