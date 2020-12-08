from django.db import models
from django.contrib.auth.models import User
from services.models import Services
from django.utils import timezone


class Review(models.Model):

    reviewed_level_type = models.ForeignKey(Services, on_delete=models.CASCADE)
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_author")
    date_of_contact = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ('reviewed_level_type',)
