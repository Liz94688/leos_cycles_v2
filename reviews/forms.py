from django import forms
from .models import Review

# Does the User need to be imported here as well?


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['level_type', 'rating', 'message']

        widgets = {
            'level_type': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please type your message in here:'}),
        }
