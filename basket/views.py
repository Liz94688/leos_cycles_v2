from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services.models import Services


@login_required
def view_basket(request):
    """ A view to return the basket """

    return render(request, 'basket/basket.html')


@login_required
def add_to_basket(request, pk):
    """ A view to add item to the basket """

    service = get_object_or_404(Services, pk=pk)

    """ Get the data from the FORM """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    """ Check if basket variable included in session """
    """ or return empty dictionary to create one """
    basket = request.session.get('basket', {})

    """ Add item to basket or update quantity """
    if pk in list(basket.keys()):
        basket[pk] += quantity
    else:
        basket[pk] = quantity
        messages.success(request, f'Added { service.level_type} to your basket.')

    """ Update variable in the session with updated version """
    request.session['basket'] = basket

    """ Redirect user back to redirect url """
    return redirect(redirect_url)


@login_required
def edit_basket(request, pk):
    """ A view to edit items in the basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[pk] = quantity
    else:
        basket.pop(pk)
        messages.success(request, 'Basket updated!')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


@login_required
def remove_from_basket(request, pk):
    """ Remove an item from the basket """

    basket = request.session.get('basket', {})
    basket.pop(pk)
    messages.success(request, 'Item removed from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
