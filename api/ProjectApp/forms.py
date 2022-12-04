from CoreApp.services.image import ImageThumbnailBaseMixin
from ProjectApp.models import ScienderProject
from django import forms


class ProjectImageManagerMixin(ImageThumbnailBaseMixin):
    def clean_image(self):
        if self.instance.image == self.cleaned_data.get('image'):
            return self.instance.image
        return self.makeImageThumbnail(self.cleaned_data.get('image'))


class ScienderUserCreateForm(forms.ModelForm, ProjectImageManagerMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(ProjectImageManagerMixin, self).__init__(coef=0.6)
    
    class Meta:
        model = ScienderProject
        fields = "__all__"
