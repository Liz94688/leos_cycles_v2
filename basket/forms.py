from django import forms
from .models import Event


class ScheduleEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['day', 'start_time',
                    'end_time', 'notes']

        day = forms.DateField(widget=forms.DateInput, input_formats=['%d/%m/%Y']),
        start_time = forms.TimeField(widget=forms.TimeInput),
        end_time = forms.TimeField(widget=forms.TimeInput),
        notes = forms.Textarea(),
