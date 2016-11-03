from django.forms import ModelForm

from .models import Image, Gallery
from .widgets import CheckboxSelectMultipleImage


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
        widgets = {
            "active_images": CheckboxSelectMultipleImage
        }
