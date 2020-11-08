from django.contrib import admin
from .models import BikeType, HandlebarType, FrameType, Bike

# Register your models here.


class BikeTypeAdmin(admin.ModelAdmin):
    list_display = (
        'bike_type',
    )


class HandlebarTypeAdmin(admin.ModelAdmin):
    list_display = (
        'handlebar_type',
    )


class FrameTypeAdmin(admin.ModelAdmin):
    list_display = (
        'frame_type',
    )


class BikeAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'bike_type',
        'bike_creation_date',
    )


admin.site.register(BikeType, BikeTypeAdmin)
admin.site.register(HandlebarType, HandlebarTypeAdmin)
admin.site.register(FrameType, FrameTypeAdmin)
admin.site.register(Bike, BikeAdmin)
