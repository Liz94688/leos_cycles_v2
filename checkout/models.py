from django.db import models
from bike.models import Bike
from services.models import Services
from basket.models import CalendarEvent


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Order'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, null=True, on_delete=models.SET_NULL)
    calendar_event = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.full_name

    class Meta:
        verbose_name_plural = 'OrderLineItem'
