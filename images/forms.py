from django import forms
from . import models

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput
        }
        """
            Users will not enter the image URL directly in the form. Instead, we will provide them with a JavaScript tool to choose an image from an external site, and our form will receive its URL as a parameter. We override the default widget of the url field to use a HiddenInput widget. This widget is rendered as an HTML input element with a type="hidden" attribute. We use this widget because we don't want this field to be visible to users.
        """