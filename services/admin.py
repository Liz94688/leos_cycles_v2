from django.contrib import admin
from .models import Services

# Register your models here.


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'level_type',
        'description',
        'price',
    )


admin.site.register(Services, ServicesAdmin)
