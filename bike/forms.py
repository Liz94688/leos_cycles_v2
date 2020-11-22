from django import forms
from .models import Bike


class CreateBikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = [
            'bike_type',
            'frame_type',
            'handlebar_type',
            'wheel_size',
            'owner_description',
            'age',
            'current',
            'bike_creation_date'
            ]

        widgets = {
            'bike_type': forms.Select(attrs={'class': 'form-control'}),
            'frame_type': forms.Select(attrs={'class': 'form-control'}),
            'handlebar_type': forms.Select(attrs={'class': 'form-control'}),
            'wheel_size': forms.Select(attrs={'class': 'form-control'}),
            'owner_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Specific details:'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'current': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
