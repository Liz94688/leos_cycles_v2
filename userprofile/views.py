from django.shortcuts import render


def userprofile(request):
    """ Display the user's profile. """

    template = 'userprofile/userprofile.html'
    context = {}

    return render(request, template, context)
