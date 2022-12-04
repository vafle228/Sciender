from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


def projectUploadPath(instance, filename: str) -> str:
    return f"projects/{instance.name}/{filename}"


def projectDefaultImage() -> InMemoryUploadedFile:
    pass
 

class ScienderProject(models.Model):
    tutor = models.OneToOneField(
        to="AuthApp.ScienderUser", 
        related_name="tutor", 
        on_delete=models.CASCADE
    )
    
    team = models.ManyToManyField(
        to="AuthApp.ScienderUser", 
        related_name="team", blank=True
    )
    
    interests = models.ManyToManyField(
        to="CoreApp.ScienceInterest", 
        related_name="interest", blank=True
    )
    
    STATUSES = (
        ("Ready", "Завершён"),
        ("Working", "В работе"),
        ("Seeking team", "Набор участников"),
    )
    DEFAULT_STATUS = "Seeking team"
    
    about       = models.TextField()
    name        = models.CharField(max_length=255)
    status      = models.CharField(max_length=255, choices=STATUSES, default=DEFAULT_STATUS)
    image       = models.ImageField(upload_to=projectUploadPath, default=projectDefaultImage)
    
    def __str__(self) -> str:
        return f"Project {self.name}"
    