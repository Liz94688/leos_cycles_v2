from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Bike(models.Model):
    BIKE_TYPE = [
        ('Road', 'Road'),
        ('Hybrid', 'Hybrid'),
        ('Mountain', 'Mountain'),
        ('BMX', 'BMX'),
        ('Childrens', 'Childrens'),
    ]

    HANDLEBAR_TYPE = [
        ('Dropdown', 'Dropdown'),
        ('Bullhorn', 'Bulhorn'),
        ('Aero', 'Aero'),
    ]

    FRAME_TYPE = [
        ('Steel', 'Steel'),
        ('Titanium', 'Titanium'),
    ]

    WHEEL_SIZE = [
        (i, i) for i in range(0, 26)
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bike_type = models.CharField(max_length=15, choices=BIKE_TYPE)
    frame_type = models.CharField(max_length=15, choices=FRAME_TYPE)
    handlebar_type = models.CharField(max_length=15, choices=HANDLEBAR_TYPE)
    wheel_size = models.IntegerField(blank=False, choices=WHEEL_SIZE)
    owner_description = models.TextField()
    age = models.IntegerField(default=0)
    bike_creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Bikes'
