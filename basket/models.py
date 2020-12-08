from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

"""

I learnt about building a simple calendar with django from here:
https://alexpnt.github.io/2017/07/15/django-calendar/

"""


class Event(models.Model):

    DAY = [(i, i) for i in range(0, 32)]

    MONTH = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sept', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December'),
    ]

    YEAR = [(i, i) for i in range(2020, 2031)]

    TIME_SLOTS = [
        ('09:00 - 12:00', '09:00 - 12:00'),
        ('12:00 - 15:00', '12:00 - 15:00'),
        ('15:00 - 18:00', '15:00 - 18:00'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField(blank=False, choices=DAY)
    month = models.CharField(max_length=5, blank=False, choices=MONTH, default='Null')
    year = models.IntegerField(blank=False, choices=YEAR, default='0000')
    time_period = models.CharField(max_length=15, blank=False, choices=TIME_SLOTS, default='00:00 - 00:00')
    notes = models.TextField()

    class Meta:
        verbose_name = u'Scheduled Events'
        verbose_name_plural = u'Scheduled Events'

    def __str__(self):
        return str(self.day)

    def check_overlap(self, fixed_time, new_time):
        overlap = False
        if new_time > fixed_time:
            overlap = False
        elif new_time < fixed_time:
            overlap = False
        elif new_time == fixed_time:
            overlap = True

        return overlap

    def clean(self):
        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.time_period, self.time_period):
                    raise ValidationError(
                        'There is an overlap with another scheduled service: ' + str(event.day)
                         + str(event.month) + str(event.year) + '-' + str(event.time_period))
