from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from reviews.models import Review
# from bike.models import Bike
from .forms import ContactDetailsForm


@login_required
def view_profile(request):
    # user_profile = User.objects.get()
    # user_profile.save()

    # bike = Bike.objects.all()
    # bike.save()

    contact_form = ContactDetailsForm()

    return render(request, 'userprofile/view_profile.html', {'contact_form': contact_form})
