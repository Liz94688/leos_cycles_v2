from django import forms
from .models import Services, Level


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        levels = Level.objects.all()
        level_types = [(c.id, c.get_level_type()) for c in levels]

        self.fields['levels'].choices = level_types
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0 text-grey'
