from django.contrib import admin
from .models import ContactUs

# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_of_contact',
        'message',
    )


admin.site.register(ContactUs, ContactUsAdmin)
