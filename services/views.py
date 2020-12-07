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
        add_level = LevelsForm(request.POST)

        # check whether it's valid:
        if add_level.is_valid():
            level = add_level.save(commit=False)
            level.save()
            messages.success(request, 'Level successfully added!')
            return redirect(reverse('add_service', args=[level.id]))
        else:
            messages.error(request, 'Failed to add Level. \
                Please ensure the form is valid.')
            add_level = LevelsForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        add_level = LevelsForm()

    context = {
        'add_level': add_level,
    }

    return render(request, 'services/add_level.html', context)


def add_service(request):
    """ Add a service to the site """
    form = ServicesForm()

    context = {
        'form': form,
    }

    return render(request, 'services/add_service.html', context)
