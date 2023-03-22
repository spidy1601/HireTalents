from django import forms
from .models import Question,Option

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = '__all__'