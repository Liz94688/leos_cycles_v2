from django.shortcuts import render, redirect


def view_basket(request):
    """ A view to return the basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, pk):
    """ A view to add item to the basket """

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

    """ Update variable in the session with uupdated version """
    request.session['basket'] = basket
    print(request.session['basket'])

    """ Redirect user back to redirect url """
    return redirect(redirect_url)
