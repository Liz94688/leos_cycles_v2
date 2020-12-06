from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def userprofile(request):
    """ Display the user's profile. """

    userprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=userprofile)
    orders = userprofile.orders.all()

    template = 'userprofile/userprofile.html'
    context = {
        'form': form,
        'orders': orders,
        # 'on_profile_page': True,
    }

    return render(request, template, context)
