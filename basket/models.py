from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

"""

I learnt about building a simple calendar with django from here:
https://alexpnt.github.io/2017/07/15/django-calendar/

"""


class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduled Events'
        verbose_name_plural = u'Scheduled Events'

    def __str__(self):
        return str(self.day)

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end):  #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  #outter limits
            overlap = True

        return overlap

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another scheduled service: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
