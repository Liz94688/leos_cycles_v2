from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

"""

I learnt about building a simple calendar with django from here:
https://alexpnt.github.io/2017/07/15/django-calendar/

"""


class CalendarEvent(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.day

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

    class Meta:
        verbose_name_plural = 'Calendar Event'
