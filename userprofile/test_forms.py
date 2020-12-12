from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_user_profile_form_can_be_created_with_required_fields(self):
        form = UserProfileForm({
            'default_phone_number': '07987665443',
            'default_postcode': 'M20 2MM',
            'default_town_or_city': 'Manchester',
            'default_street_address1': '1 Manchester Road',
            'default_street_address2': 'Didsbury',
            'default_county': 'Lancashire',
        })
        self.assertTrue(form.is_valid())
