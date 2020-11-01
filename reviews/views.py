from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReviewForm
from django.utils import timezone

# Create your views here.


@login_required
def add_review(request):
    """ A view to return the review page"""
    # import Services, get the id and save here
    # level_type = get_object_or_404(Services, id=id)
    # import get_object_or_404 at the top
    # level_type.save()
    # can then be used below in review.level_type service

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_review_form = ReviewForm(request.POST)

        # check whether it's valid:
        if user_review_form.is_valid():
            review = user_review_form.save(commit=False)
            review.author = request.user
            review.date_of_contact = timezone.now()
            # review.level_type = level_type
            review.save()
            return render(request, 'home/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        user_review_form = ReviewForm()

    return render(request, 'reviews/reviews.html', {'user_review_form': user_review_form})
