from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BikeType(models.Model):

    BIKE_TYPE = [
        ('Road', 'Road'),
        ('Hybrid', 'Hybrid'),
        ('Mountain', 'Mountain'),
        ('BMX', 'BMX'),
        ('Childrens', 'Childrens'),
        ('Other', 'Other'),
    ]

    bike_type = models.CharField(max_length=15, choices=BIKE_TYPE)

    def __str__(self):
        return self.bike_type


class HandlebarType(models.Model):

    HANDLEBAR_TYPE = [
        ('Flat', 'Flat'),
        ('Riser', 'Riser'),
        ('Drop', 'Drop'),
        ('Bullhorn', 'Bullhorn'),
        ('Aero', 'Aero'),
        ('Cruiser', 'Cruiser'),
        ('Butterfly', 'Butterfly'),
        ('Other', 'Other'),
    ]

    handlebar_type = models.CharField(max_length=15, choices=HANDLEBAR_TYPE)

    def __str__(self):
        return self.handlebar_type


class FrameType(models.Model):

    FRAME_TYPE = [
        ('Carbon Fiber', 'Carbon Fiber'),
        ('Steel', 'Steel'),
        ('Titanium', 'Titanium'),
        ('Aluminum', 'Aluminum'),
        ('Other', 'Other'),
    ]

    frame_type = models.CharField(max_length=15, choices=FRAME_TYPE)

    def __str__(self):
        return self.frame_type


class Bike(models.Model):

    WHEEL_SIZE = [
        (i, i) for i in range(0, 30)
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bike_type = models.ForeignKey(BikeType, on_delete=models.CASCADE)
    frame_type = models.ForeignKey(FrameType, on_delete=models.CASCADE)
    handlebar_type = models.ForeignKey(HandlebarType, on_delete=models.CASCADE)
    wheel_size = models.IntegerField(blank=False, choices=WHEEL_SIZE)
    owner_description = models.TextField()
    age = models.IntegerField(default=0)
    bike_creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Bikes'
