from django.db import models
from django.contrib.auth.models import User
from bike.models import Bike


class UserProfile(models.Model):

    '''extending the user Model using a OneToOneField'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    street_address_line_one = models.CharField(max_length=80, blank=True)
    street_address_line_two = models.CharField(max_length=80, blank=True)
    street_address_line_three = models.CharField(max_length=80, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    contact_by_phone = models.BooleanField(blank=True, default=False)
    bikes = models.ManyToManyField(Bike, blank=True)

    def __str__(self):
        return self.user.username
