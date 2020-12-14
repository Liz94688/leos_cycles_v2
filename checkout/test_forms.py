from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_create_order_with_required_fields_filled(self):

        form = OrderForm({
            'full_name': 'test',
            'phone_number': '07123456789',
            'country': 'United Kingdom',
            'postcode': 'M20 2MM',
            'town_or_city': 'Manchester',
            'street_address1': '123 Manchester Road',
            'county': 'Lancashire',
            'preferred_service_date': '2021-02-02',
        })
        self.assertTrue(form.is_valid())

    def test_correct_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
