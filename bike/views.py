from django.shortcuts import render, redirect, reverse, \
    get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bike
from .forms import CreateBikeForm


@login_required
def view_all_bikes(request):

    all_bikes = Bike.objects.filter(owner=request.user)

    context = {
        'all_bikes': all_bikes,
    }

    return render(request, 'bike/view_all_bikes.html', context)


@login_required
def add_bike(request):
    """ A view for the user to add a bike to their profile """

    if not request.user.is_authenticated:
        messages.error(request, 'Access denied.\
             Only members can add a bike!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        add_bike = CreateBikeForm(request.POST)

        # check whether it's valid:
        if add_bike.is_valid():
            bike = add_bike.save(commit=False)
            bike.owner = request.user
            bike.save()
            messages.success(request, 'Bike has been successfully added!')
            redirect(reverse('view_all_bikes'))
            return render(request, 'home/index.html')
        else:
            messages.error(request, 'Failed to add bike. \
                Please ensure the form is valid.')
            add_bike = CreateBikeForm()
    else:
        add_bike = CreateBikeForm()

    context = {
        'add_bike': add_bike,
    }

    return render(request, 'bike/add_bike.html', context)


@login_required
def edit_bike(request, bike_id):
    """ A view allowing the user to edit a bike recorded on their profile """

    if not request.user.is_authenticated:
        messages.error(request, 'Access denied.\
             Only members can edit a bike!')
        return redirect(reverse('home'))

    bike = get_object_or_404(Bike, pk=bike_id)
    if request.method == 'POST':
        form = CreateBikeForm(request.POST, instance=bike)

        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, 'Bike has been successfully edited!')
            return redirect(reverse('view_all_bikes'))
        else:
            messages.error(request, 'Failed to edit bike. \
                Please ensure the form is valid.')
    else:
        form = CreateBikeForm(instance=bike)
        messages.info(request, f'You are editing {bike.type}')

    context = {
        'bike': bike,
        'form': form,
    }

    return render(request, 'bike/edit_bike.html', context)


@login_required
def delete_bike(request, bike_id):
    """ A view allowing users to delete a recorded bike from their profile """
    if not request.user.is_authenticated:
        messages.error(request, 'Access denied.\
             Only members can delete a bike.')
        return redirect(reverse('home'))

    bike = get_object_or_404(Bike, pk=bike_id)
    bike.pop(bike_id)

    messages.info(request, f'{bike.bike_type} was successfully deleted.')
    return redirect(reverse('view_all_bikes'))
