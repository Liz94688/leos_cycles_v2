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
        fields = (
            'email',
            'message'
        )

    def __init__(self, *args, **kwargs):

        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email Address',
            'message': 'Message',
        }

        self.fields['email'].widget.attrs['autofocus'] = False
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False
