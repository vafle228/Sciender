from django.db import models


class PreMatch(models.Model):
    to_user = models.ForeignKey(
        to="AuthApp.ScienderUser", 
        related_name="to_user",
        on_delete=models.CASCADE
    )
    
    from_user = models.ForeignKey(
        to="AuthApp.ScienderUser", 
        related_name="from_user", 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"PreMatch from {self.from_user} to {self.to_user}"


class ScienderMatch(models.Model):
    user1 = models.ForeignKey(
        to="AuthApp.ScienderUser", 
        related_name="user1", 
        on_delete=models.CASCADE
    )
    
    user2 = models.ForeignKey(
        to="AuthApp.ScienderUser", 
        related_name="user2", 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"Match {self.user1} with {self.user2}"
