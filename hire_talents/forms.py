from django import forms
from .models import DeveloperImage

class DeveloperForm(forms.ModelForm):
    developer_image = forms.ImageField()
    class Meta:
        model = DeveloperImage
        fields=['developer_image',]
