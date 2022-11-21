from django.db import models


class WorkLink(models.Model):
    link = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"Link number {self.id}"


class ScienceInterests(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"Science interest {self.name}"
