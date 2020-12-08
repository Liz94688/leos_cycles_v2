from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'created_by',
        'day',
        'month',
        'year',
        'time_period',
        'notes',
    )


admin.site.register(Event, EventAdmin)
