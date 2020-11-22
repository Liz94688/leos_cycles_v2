from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Services
from bike.models import Bike

""" I leart about how context processors work from the CI tutorials
Taken from the tutorials source code
If ANY changes made to code/wording, needs to alson be changed
in settings.py """


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    bike = Bike.objects.all()

    """ Access the basket in the current session
    Use to populate values of variables above  """

    basket = request.session.get('basket', {})

    for pk, quantity in basket.items():
        product = get_object_or_404(Services, pk=pk)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'pk': pk,
            'quantity': quantity,
            'product': product,
            'bike': bike,
        })

    if total < settings.FREE_SERVICE_CHARGE_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_SERVICE_CHARGE_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_SERVICE_CHARGE_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'bike': bike,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_SERVICE_CHARGE_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
