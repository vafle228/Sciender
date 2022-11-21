from django.db import models


class ScienderScience(models.Model):
    job_title           = models.CharField(max_length=255, blank=True)
    academic_title      = models.CharField(max_length=255, blank=True)
    academic_degree     = models.CharField(max_length=255, blank=True)
    qualifying_links    = models.ManyToManyField(to="CoreApp.WorkLink", blank=True)
    
    class Meta:
        abstract = True


class ScienderStudent(models.Model):
    user = models.OneToOneField(
        to="AuthApp.ScienderUser", 
        related_name="student_user", 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"ScienderStudent from {self.user}"


class ScienderGraduateStudent(models.Model):
    user = models.OneToOneField(
        to="AuthApp.ScienderUser",
        related_name="graduate_user", 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"ScienderGraduateStudent from {self.user}"


class ScienderScienceTutor(ScienderScience):
    user = models.OneToOneField(
        to="AuthApp.ScienderUser", 
        related_name="tutor_user", 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"ScienderScienceTutor from {self.user}"


class ScienderScienceWorker(ScienderScience):
    user = models.OneToOneField(
        to="AuthApp.ScienderUser", 
        related_name="worker_user", 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"ScienderScienceWorker from {self.user}"
