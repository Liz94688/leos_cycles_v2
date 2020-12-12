from django.test import TestCase
from .models import UserProfile
from django.contrib.auth.models import User


class TestUserProfileModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="username", password="password1234")

    def test_can_create_profile(self):
        userprofile = UserProfile(
            user=self.user,
            default_phone_number='07986554332',
            default_street_address1='123 Manchester Road',
            default_street_address2='Didsbury',
            default_town_or_city='Manchester',
            default_county='Lancashire',
            default_postcode='M20 2MM',
            default_country='United Kingdom',
        )
        self.assertEqual(userprofile.user.username, 'username')
        self.assertEqual("username", str(userprofile))
