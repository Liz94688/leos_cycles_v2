from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'level_type',
        'rating',
        'date_of_contact',
    )


admin.site.register(Review, ReviewAdmin)
