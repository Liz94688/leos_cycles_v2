from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'bike',
    )


class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'service',
        'calendar_event',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
