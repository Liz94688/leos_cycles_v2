from django import forms
from .models import Services, Level


class LevelsForm(forms.Form):
    level_type = forms.CharField(max_length=15)


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'
