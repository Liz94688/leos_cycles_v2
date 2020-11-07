from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from reviews.models import Review
# from bike.models import Bike
from .forms import UserProfileForm


@login_required
def view_profile(request):
    # user_profile = User.objects.get()
    # user_profile.save()

    # bike = Bike.objects.all()
    # bike.save()

    user_profile = UserProfileForm()

    return render(request, 'userprofile/view_profile.html',
        {'user_profile': user_profile})
