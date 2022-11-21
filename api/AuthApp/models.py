from django.contrib.auth.models import AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


class BasicUser(AbstractUser):
    first_name, last_name, date_joined = None, None, None
    
    def __str__(self) -> str:
        return f"Basic user {self.username}"


def userUploadPath(instance, filename: str) -> str:
    return f'user/{instance.user.username}/{filename}'


def userDefaultImage() -> InMemoryUploadedFile:
    pass


class ScienderUser(models.Model):
    user        = models.OneToOneField("BasicUser", related_name="user", on_delete=models.CASCADE)
    
    name        = models.CharField(max_length=255)
    surname     = models.CharField(max_length=255)
    patronymic  = models.CharField(max_length=255, blank=True)
    
    STATUSES = (
        ("Free", "Свободен"),
        ("Working", "В работе"),
        ("Seeking team", "В поиске команды"),
        ("Seeking project", "В поиске проекта"),
    )
    DEFAULT_STATUS = "Free"
    
    work_links = models.ManyToManyField(
        to="CoreApp.WorkLink", 
        related_name="work_links", blank=True
    )
    
    interests = models.ManyToManyField(
        to="CoreApp.ScienceInterests", 
        related_name="user_interests", blank=True
    )
    
    about       = models.TextField(blank=True)
    specialty   = models.CharField(max_length=255, blank=True)
    image       = models.ImageField(upload_to=userUploadPath, default=userDefaultImage)
    status      = models.CharField(max_length=255, choices=STATUSES, default=DEFAULT_STATUS)


    def __str__(self) -> str:
        return f"Sciender user from {self.user}"
