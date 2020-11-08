from django.contrib import admin
from .models import CalendarEvent


class CalendarEventAdmin(admin.ModelAdmin):
    list_display = (
        'created_by',
        'day',
        'start_time',
        'end_time',
        'notes',
    )


admin.site.register(CalendarEvent, CalendarEventAdmin)
