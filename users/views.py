from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.


def register_view(request):
    """ A view to return the register page"""

    if request.method == 'POST':
        reg = RegisterForm(request.POST)

        if reg.is_valid():
            reg = reg.save(commit=False)
            reg.save()
            messages.success(request, 'User Registered')
    else:
        reg = RegisterForm()
    return render(request, 'register.html', {'reg': reg})
