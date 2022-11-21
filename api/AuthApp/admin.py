from AuthApp.forms import BasicUserChangeForm, BasicUserCreationForm
from AuthApp.models import BasicUser, ScienderUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class BasicUserAdmin(UserAdmin):
    model = BasicUser
    
    form = BasicUserChangeForm
    add_form = BasicUserCreationForm
    
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('username', 'email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'is_staff', 'password1', 'password2')
    }))
    search_fields = ('email',); ordering = ('email',)


admin.site.register(ScienderUser)
admin.site.register(BasicUser, BasicUserAdmin)
