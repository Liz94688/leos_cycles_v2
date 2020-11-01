from django.db import models

# Create your models here.


class Services(models.Model):
    LEVEL_TYPE = [
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Premium', 'Premium'),
    ]

    level_type = models.CharField(max_length=15, choices=LEVEL_TYPE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.level_type

    class Meta:
        verbose_name_plural = 'Services'
