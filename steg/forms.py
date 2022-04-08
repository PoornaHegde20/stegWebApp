from django import forms

from steg.models import LSBEncode, LSBDecode


class ImageFormEncode(forms.ModelForm):
    message = forms.CharField(label='Secret Message', max_length=1000)
    # CHOICES = [('LSB', 'LSB'),
    #            ('Addition', 'Addition')]


    # algorithm = forms.ChoiceField(label="Which algorithm do you want to choose?", choices=CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = LSBEncode
        fields = ["inputImagePath"]
        

class ImageFormDecode(forms.ModelForm):
    CHOICES = [('LSB', 'LSB'),
               ('Addition', 'Addition')]

    algorithm = forms.ChoiceField(label="Which algorithm do you want to choose?", choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = LSBDecode
        fields = ["inputImagePath"]
