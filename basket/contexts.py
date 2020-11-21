from decimal import Decimal
from django.conf import settings

""" I leart about how context processors work from the CI tutorials """
""" Taken from the tutorials source code """
""" If ANY changes made to code/wording, needs to be changed """
""" in settings.py """


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

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
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_SERVICE_CHARGE_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
