from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from services.models import Services
from .forms import ReviewForm
from django.utils import timezone
from django.contrib import messages


@login_required
def add_review(request):
    """ A view to return the review page"""
    # services = get_object_or_404(Services)
    # services.save()
    # remember to include pk as an argument above, after request
    # need to find out how to get the pk into the url...

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        user_review_form = ReviewForm(request.POST)

        # check whether it's valid:
        if user_review_form.is_valid():
            review = user_review_form.save(commit=False)
            review.author = request.user
            # review.level_type = level_type
            review.date_of_contact = timezone.now()
            review.save()
            messages.success(request, 'Review added!')
            return render(request, 'home/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        user_review_form = ReviewForm()

    context = {
        'user_review_form': user_review_form,
    }

    return render(request, 'reviews/reviews.html', context)
