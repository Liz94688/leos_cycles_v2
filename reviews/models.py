from django.db import models
from django.contrib.auth.models import User
from services.models import Services
from django.utils import timezone


class Review(models.Model):

    CHOICES = [
        (i, i) for i in range(0, 6)
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    level_type = models.ForeignKey(Services, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=False, choices=CHOICES)
    message = models.TextField()
    date_of_contact = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ('level_type', '-rating',)
