from django.contrib import admin
from .models import Level, Services

# Register your models here.


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'level_type',
    )


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'level_type',
        'description',
        'price',
        'total_reviews',
        'total_ratings',
    )


admin.site.register(Level, LevelAdmin)
admin.site.register(Services, ServicesAdmin)
