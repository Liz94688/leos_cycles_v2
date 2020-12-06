from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def userprofile(request):
    """ Display the user's profile. """

    userprofile = get_object_or_404(UserProfile, user=request.user)

    template = 'userprofile/userprofile.html'
    context = {
        'userprofile': userprofile,
    }

    return render(request, template, context)
