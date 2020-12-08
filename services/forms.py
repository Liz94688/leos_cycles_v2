from django import forms
from .models import Services, Level


class LevelsForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = '__all__'


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'
