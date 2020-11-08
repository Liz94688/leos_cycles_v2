from django.db import models

# Create your models here.


class Level(models.Model):

    LEVEL_TYPE = [
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Premium', 'Premium'),
    ]

    level_type = models.CharField(max_length=15, choices=LEVEL_TYPE)

    def __str__(self):
        return str(self.level_type)


class Services(models.Model):

    level_type = models.ForeignKey(Level, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total_reviews = models.IntegerField(default=0)
    total_ratings = models.IntegerField(default=0)

    def __str__(self):
        return str(self.level_type)

    class Meta:
        verbose_name_plural = 'Services'
