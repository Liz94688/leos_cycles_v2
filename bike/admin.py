from django.contrib import admin
from .models import Bike

# Register your models here.


class BikeAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'bike_type',
        'bike_creation_date',
    )


admin.site.register(Bike, BikeAdmin)
