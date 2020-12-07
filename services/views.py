from django.shortcuts import render,  redirect, reverse, \
    get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Services
from reviews.models import Review
from .forms import LevelsForm, ServicesForm


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


def add_level(request):
    """ A view for admin to add a level to the site """

    if request.method == 'POST':
        form = LevelsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, 'Level successfully added!')
            return redirect(reverse('add_level'))
        else:
            messages.error(request, 'Failed to add Level. \
                Please ensure the form is valid.')
            form = LevelsForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LevelsForm()

    context = {
        'form': form,
    }

    return render(request, 'services/add_level.html', context)


def add_service(request):
    """ A view for admin to add a service to the site """

    if request.method == 'POST':
        form = ServicesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, 'Service successfully added!')
            return redirect(reverse('add_service'))
        else:
            messages.error(request, 'Failed to add Service. \
                Please ensure the form is valid.')
            form = ServicesForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ServicesForm()

    context = {
        'form': form,
    }

    return render(request, 'services/add_service.html', context)
