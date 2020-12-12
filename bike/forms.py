from django import forms
from .models import Bike


class CreateBikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = (
            'bike_type',
            'frame_type',
            'handlebar_type',
            'frame_size',
            'owner_description',
            'age',
            'current',
            )

    def __init__(self, *args, **kwargs):

        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'bike_type': 'Bike Type',
            'frame_type': 'Frame Type',
            'handlebar_type': 'Handlebar Type',
            'frame_size': 'Frame Size',
            'owner_description': 'Any specific details about the bike',
            'age': 'Age - Years',
            'current': 'Current',
        }

        self.fields['bike_type'].widget.attrs['autofocus'] = True
        self.fields['current'].label = ''
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
