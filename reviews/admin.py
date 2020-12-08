from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'reviewed_level_type',
        'message',
        'author',
        'date_of_contact',
    )


admin.site.register(Review, ReviewAdmin)
