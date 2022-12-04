from django.contrib import admin
from ProjectApp.models import ScienderProject
from ProjectApp.forms import ScienderUserCreateForm


class ScienderProjectAdmin(admin.ModelAdmin):
    form = ScienderUserCreateForm


admin.site.register(ScienderProject, ScienderProjectAdmin)
