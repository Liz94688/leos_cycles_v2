from django.test import TestCase
from .models import Bike, BikeType, FrameType, HandlebarType
from django.contrib.auth.models import User


class TestReviewModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="username", password="password1234")

        test_bike_type = BikeType.objects.create(bike_type='Type')
        test_frame_type = FrameType.objects.create(frame_type='Frame')
        test_handlebar_type = HandlebarType.objects.create(handlebar_type='Handlebar')

        self.bike = Bike.objects.create(
            owner=self.user,
            bike_type=test_bike_type,
            frame_type=test_frame_type,
            handlebar_type=test_handlebar_type,
            frame_size='Small',
            owner_description='Random message',
            age=0,
            current=True,
            bike_creation_date='2020-01-01')

    def test_can_create_bike(self):
        bike = Bike(
            owner=self.user,
            bike_type=self.bike.bike_type,
            frame_type=self.bike.frame_type,
            handlebar_type=self.bike.handlebar_type,
            frame_size='Small',
            owner_description='Random message',
            age=0,
            current=True,
            bike_creation_date='2020-01-01 00:00:00'
        )
        self.assertEqual(bike.bike_type.bike_type, 'Type')
