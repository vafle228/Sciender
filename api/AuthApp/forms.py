from AuthApp.models import BasicUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class BasicUserCreationForm(UserCreationForm):
    class Meta:
        model = BasicUser
        fields = ('username', 'email', 'is_staff')


class BasicUserChangeForm(UserChangeForm):
    class Meta:
        model = BasicUser
        fields = ('username', 'email', 'is_staff')
