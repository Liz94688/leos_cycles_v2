from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from reviews.models import Review
from bike.models import Bike
from .forms import ContactDetailsForm
from django.utils import timezone
from django.contrib import messages


@login_required
def view_profile(request):
    """ A view to return the user profile page """

    user_profile = User.objects.get(username=request.user.username)
    user_profile.save()

    bike = Bike.objects.all()

    user_reviews = Review.objects.filter(author=request.user)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        contact_details_form = ContactDetailsForm(request.POST)

        # check whether it's valid:
        if contact_details_form.is_valid():
            contact_details = contact_details_form.save(commit=False)
            contact_details.date_of_contact = timezone.now()
            contact_details.user = request.user
            contact_details.save()
            messages.success(request, 'Your contact details have been saved')
            return render(request, 'userprofile/view_profile.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        contact_details_form = ContactDetailsForm()

    return render(request, 'userprofile/view_profile.html',
        {'user_profile': user_profile,
        'bike': bike,
        'user_reviews': user_reviews,
        'contact_details_form': contact_details_form})
