from django.shortcuts import render, redirect, reverse, \
    get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from .forms import ReviewForm


@login_required
def add_review(request):
    """ A view allowing the user to add a review """

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.date_of_contact = timezone.now()
            review.save()
            messages.success(request, 'Review successfully added!')
            return redirect(reverse('userprofile'))
    # if a GET (or any other method) we'll create a blank form
    else:
        review_form = ReviewForm()

    context = {
        'review_form': review_form,
    }

    return render(request, 'reviews/add_review.html', context)
