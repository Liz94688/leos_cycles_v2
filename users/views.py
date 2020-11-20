from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register_view(request):
    """ A view to return the register page"""

    if request.method == 'POST':
        register = RegisterForm(request.POST)

        if register.is_valid():
            register = register.save(commit=False)
            register.save()
            messages.success(request, 'User Registered')
            return redirect(reverse('index'))
    else:
        register = RegisterForm()
    return render(request, 'register.html', {'register': register})
