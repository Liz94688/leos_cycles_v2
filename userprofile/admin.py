from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'town_or_city',
        'postcode',
        'telephone',
        'contact_by_email',
        'contact_by_phone',
    )


admin.site.register(UserProfile, UserProfileAdmin)
