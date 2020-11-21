from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateBikeForm


@login_required
def add_bike(request):
    """ A view to return the add_bike page"""

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        add_bike = CreateBikeForm(request.POST)

        # check whether it's valid:
        if add_bike.is_valid():
            bike = add_bike.save(commit=False)
            bike.owner = request.user
            bike.save()
            return render(request, 'home/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        add_bike = CreateBikeForm()

    return render(request, 'bike/add_bike.html', {'add_bike': add_bike})







""" A view to return the edit bike page """
