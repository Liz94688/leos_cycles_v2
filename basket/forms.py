from django import forms
from .models import Event


class ScheduleEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'day',
            'month',
            'year',
            'time_period',
            'notes',
        )

    def __init__(self, *args, **kwargs):

        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'day': 'Day',
            'month': 'Month',
            'year': 'Year',
            'time_period': 'Time Slot',
            'notes': 'Directions for our engineer:',
        }

        self.fields['day'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
