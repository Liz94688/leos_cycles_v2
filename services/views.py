from django.shortcuts import render
from .models import Services

# Create your views here.


def view_all_services(request):
    service_level = Services.objects.all()

    return render(request, 'services/services.html', {'service_level': service_level})
