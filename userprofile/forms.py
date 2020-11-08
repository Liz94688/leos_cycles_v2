from django import forms
from .models import UserProfile


class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'street_address_line_one',
            'street_address_line_two',
            'street_address_line_three',
            'town_or_city',
            'postcode',
            'telephone',
            'contact_by_phone',
            ]

        widgets = {
            'street_address_line_one': forms.TextInput(attrs={'class': 'form-control'}),
            'street_address_line_two': forms.TextInput(attrs={'class': 'form-control'}),
            'street_address_line_three': forms.TextInput(attrs={'class': 'form-control'}),
            'town_or_city': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact_by_phone': forms.CheckboxInput(attrs={'class': 'form-control'}),
            }
