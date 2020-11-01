from django.db import models
from django.utils import timezone

# Create your models here.


class ContactUs(models.Model):
    email = models.EmailField(max_length=80)
    message = models.TextField()
    date_of_contact = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email + ' | ' + self.message

    class Meta:
        verbose_name_plural = 'Contact Us'
