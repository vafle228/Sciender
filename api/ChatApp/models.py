from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile


class ChatMessage(models.Model):
    sender = models.ForeignKey(
        to="AuthApp.ScienderUser", 
        related_name="sender", 
        on_delete=models.CASCADE
    )
    
    text    = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Message from {self.sender}"


def backgroundUploadPath(instance, filename: str) -> str:
    return f"chats/{instance.name}/{filename}"


def backgroundDefaultImage(instance, filename: str) -> InMemoryUploadedFile:
    pass


class ScienderChat(models.Model):
    name        = models.CharField(max_length=255)
    users       = models.ManyToManyField(to="AuthApp.ScienderUser", related_name="users")
    messages    = models.ManyToManyField(to="ChatMessage", related_name="messages", blank=True)
    background  = models.ImageField(default=backgroundUploadPath, upload_to=backgroundDefaultImage)
    
    def __str__(self) -> str:
        return f"Chat {self.name}"
    
    @property
    def isPersonal(self) -> bool:
        return len(self.users.all()) == 2  # if only 2 users in chat
