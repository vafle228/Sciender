from django.contrib import admin
from ProfileApp.models import (ScienderGraduateStudent, ScienderScienceTutor,
                               ScienderScienceWorker, ScienderStudent)


admin.site.register(ScienderStudent)
admin.site.register(ScienderScienceTutor)
admin.site.register(ScienderScienceWorker)
admin.site.register(ScienderGraduateStudent)
