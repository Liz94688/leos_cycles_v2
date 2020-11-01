from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# Need to import the Services, once they've been created
# From services.models import Services
# Use as a FK rather than the choices option
# service_type = models.ForeignKey(Services,
# default='', on_delete=models.CASCADE)


class Review(models.Model):
    SERVICE_TYPE = [
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Premium', 'Premium'),
    ]

    CHOICES = [
        (i, i) for i in range(0, 6)
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    level_type = models.CharField(max_length=15, choices=SERVICE_TYPE)
    rating = models.IntegerField(blank=False, choices=CHOICES)
    message = models.TextField()
    date_of_contact = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ('level_type', '-rating',)
