from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from services.models import Services


def view_basket(request):
    """ A view to return the basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ A view to add item to the basket """

    service = get_object_or_404(Services, pk=item_id)

    """ Get the data from the FORM """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    """ Check if basket variable included in session """
    """ or return empty dictionary to create one """
    basket = request.session.get('basket', {})

    """ Add item to basket or update quantity """
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added { service.level_type} to your basket.')

    """ Update variable in the session with updated version """
    request.session['basket'] = basket

    """ Redirect user back to redirect url """
    return redirect(redirect_url)


def edit_basket(request, item_id):
    """ A view to edit items in the basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)
        messages.success(request, 'Basket updated!')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove an item from the basket """

    basket = request.session.get('basket', {})
    basket.pop(item_id)
    messages.success(request, 'Item removed from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
