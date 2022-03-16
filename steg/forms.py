from django import forms

from steg.models import lsbEncoding


class ImageForm(forms.ModelForm):
    class Meta:
        model = lsbEncoding
        fields = ["inputImageName", "inputImagePath"]
