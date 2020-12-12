from django.test import TestCase
from .forms import OrderForm

# Create your tests here.


class TestOrderForm(TestCase):

    def test_create_order_with_required_fields_filled(self):
        form = OrderForm({
            'full_name': 'test',
            'phone_number': '07123 456789',
            'street_address1': '123 Manchester Road',
            'town_or_city': 'Manchester',
            'postcode': 'M20 2MM',
            'country': 'United Kingdom'
        })
        self.assertTrue(form.is_valid())

    def test_correct_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
