from django.db import models


class ScienderAdmin(models.Model):
    user = models.OneToOneField(
        to="AuthApp.BasicUser", 
        related_name="admin_user",
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"Sciender admin from {self.user}"


class VerificationRequest(models.Model):
    user = models.OneToOneField(
        to="AuthApp.ScienderUser", 
        related_name="user_request", 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"VerificationRequest from {self.user}"
