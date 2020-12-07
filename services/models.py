from django.db import models

# Create your models here.


class Level(models.Model):
    level_type = models.CharField(max_length=15)

    def __str__(self):
        return str(self.level_type)


class Services(models.Model):

    level_type = models.ForeignKey(Level, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.level_type)

    class Meta:
        verbose_name_plural = 'Services'
