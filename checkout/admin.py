from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'postcode',
        'date',
        'grand_total',
    )


class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'service',
        'quantity',
        'bike',
        'calendar_event',
        'lineitem_total',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
