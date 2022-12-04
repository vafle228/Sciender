from CoreApp.services.image import ImageThumbnailBaseMixin


class UserImageManagerMixin(ImageThumbnailBaseMixin):
    def clean_image(self):
        if self.instance.image == self.cleaned_data.get('image'):
            return self.instance.image
        return self.makeImageThumbnail(self.cleaned_data.get('image'))
