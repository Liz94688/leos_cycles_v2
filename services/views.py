from django.shortcuts import render, get_object_or_404
from .models import Services
from reviews.models import Review


def service_list(request):
    """ A view to return the all services page """

    service_list = Services.objects.all()

    context = {
        'service_list': service_list,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, pk):
    """ A view to return the details of each service """

    service_detail = get_object_or_404(Services, pk=pk)
    reviews = Review.objects.filter(level_type=pk).order_by('-date_of_contact')

    context = {
        'service_detail': service_detail,
        'reviews': reviews,
    }

    return render(request, 'services/service_details.html', context)
