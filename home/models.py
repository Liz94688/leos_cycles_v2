from django.db import models
from datetime import datetime

# Create your models here.


class ContactUs(models.Model):
    email = models.EmailField(max_length=80)
    message = models.TextField()
    date_of_contact = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name
