from django import forms
from .models import ContactUs

"""

I found out about widgets from Django documentation:
https://docs.djangoproject.com/en/3.1/ref/forms/widgets/

I found about about styling Django forms here:
https://stackoverflow.com/questions/5827590/css-styling-in-django-forms
and here:
https://www.youtube.com/watch?v=6-XXvUENY_8&feature=emb_logo

"""


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'message']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please type your message in here:'}),
        }
