from django.utils.html import mark_safe
from django.conf import settings
from django.forms import widgets

class ImageCheckboxChoiceInput(widgets.CheckboxChoiceInput):
        input_type = 'checkbox'

        def __init__(self, *args, **kwargs):
            super(ImageCheckboxChoiceInput, self).__init__(*args, **kwargs)
            self.choice_label = mark_safe("<img src=\"{}{}\">".format(settings.MEDIA_URL, self.choice_label))


class ImageCheckboxFieldRenderer(widgets.ChoiceFieldRenderer):
    choice_input_class = ImageCheckboxChoiceInput


class CheckboxSelectMultipleImage(widgets.CheckboxSelectMultiple):
    renderer = ImageCheckboxFieldRenderer


