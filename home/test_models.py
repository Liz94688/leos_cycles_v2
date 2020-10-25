from django.test import TestCase
from .models import ContactUs

# Create your tests here.


class TestHomeModels(TestCase):

    def test_contact_us_form_can_be_created(self):
        form = ContactUs(
            email='email@email.com',
            message='test message',
            date_of_contact='2020-10-25',
        )

        self.assertEqual(form.email, 'email@email.com')
