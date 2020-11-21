from django.shortcuts import render
from .forms import ContactUsForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def index(request):
    """ A view to return the index page"""

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page"""

    return render(request, 'home/about.html')


def contact(request):
    """ A view to return the contact page"""

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        contact_us_form = ContactUsForm(request.POST)

        # check whether it's valid:
        if contact_us_form.is_valid():
            contact = contact_us_form.save(commit=False)
            contact.date_of_contact = timezone.now()
            contact.save()
            messages.success(request, 'We have received your message')
            return render(request, 'home/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        contact_us_form = ContactUsForm()

    context = {
        'contact_us_form': contact_us_form
    }

    return render(request, 'home/contact.html', context)
