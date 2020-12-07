from django.shortcuts import render,  redirect, reverse, \
    get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Services, Level
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


def edit_level(request, level_id):
    """ A view for admin to edit a level on the site """
    level = get_object_or_404(Level, pk=level_id)

    if request.method == 'POST':
        form = LevelsForm(request.POST, instance=level)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated level!')
            return redirect(reverse('service_detail', args=[level.id]))
        else:
            messages.error(request, 'Failed to update level. Please ensure the form is valid.')
    else:
        form = LevelsForm(instance=level)
        messages.info(request, f'You are editing the {level.level_type} level')

    context = {
        'form': form,
        'level': level,
    }

    return render(request, 'services/edit_level.html', context)


def edit_service(request, service_id):
    """ A view for admin to edit a service on the site """

    service = get_object_or_404(Services, pk=service_id)

    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ServicesForm(instance=service)
        messages.info(request, f'You are editing the {service.level_type} service')

    context = {
        'form': form,
        'service': service,
    }

    return render(request, 'services/edit_service.html', context)
