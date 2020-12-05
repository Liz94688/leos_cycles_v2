from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Services
from reviews.models import Review


def service_list(request):
    """ A view to return the all services page """

    service_list = Services.objects.all()

    context = {
        'service_list': service_list,
    }

    return render(request, 'services/services.html', context)


@login_required
def service_detail(request, service_id):
    """ A view to return the details of each service """

    service = get_object_or_404(Services, pk=service_id)
    reviews = Review.objects.filter(level_type=service_id).order_by('-date_of_contact')

    context = {
        'service': service,
        'reviews': reviews,
    }

    return render(request, 'services/service_details.html', context)
