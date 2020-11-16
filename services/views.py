from django.shortcuts import render, get_object_or_404
from .models import Services
from reviews.models import Review


def service_list(request):
    services = Services.objects.all()
    return render(request, 'services/services.html', {'services': services})


def service_detail(request, pk):
    service_detail = get_object_or_404(Services, pk=pk)
    reviews = Review.objects.filter(level_type=pk).order_by('-date_of_contact')

    return render(request, 'services/service_details.html',
        {'service_detail': service_detail,
        'reviews': reviews})
