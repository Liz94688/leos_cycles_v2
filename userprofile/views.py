from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from reviews.models import Review
from bike.models import Bike


@login_required
def userprofile(request):
    """ Display the user's profile. """

    userprofile = get_object_or_404(UserProfile, user=request.user)

    reviewed_services = list(Review.objects.filter(
        author=request.user))

    bikes = Bike.objects.filter(owner=request.user)

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
        'reviewed_services': reviewed_services,
        'bikes': bikes,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
