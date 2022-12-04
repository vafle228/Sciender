from AuthApp.models import BasicUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from CoreApp.services.image import ImageThumbnailBaseMixin
from AuthApp.models import ScienderUser
from django import forms


class BasicUserCreationForm(UserCreationForm):
    class Meta:
        model = BasicUser
        fields = ('username', 'email', 'is_staff')


class BasicUserChangeForm(UserChangeForm):
    class Meta:
        model = BasicUser
        fields = ('username', 'email', 'is_staff')


class UserImageManagerMixin(ImageThumbnailBaseMixin):
    def clean_image(self):
        if self.instance.image == self.cleaned_data.get('image'):
            return self.instance.image
        return self.makeImageThumbnail(self.cleaned_data.get('image'))


class ScienderUserCreateForm(forms.ModelForm, UserImageManagerMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(UserImageManagerMixin, self).__init__(coef=0.5)
    
    class Meta:
        model = ScienderUser
        fields = "__all__"
