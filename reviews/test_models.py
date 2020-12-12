from django.test import TestCase
from .models import Review
from django.contrib.auth.models import User
from services.models import Level, Services


class TestReviewModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="username", password="password1234")

        test_reviewed_level_type = Level.objects.create(level_type='Basic')

        self.service = Services.objects.create(
            level_type=test_reviewed_level_type,
            description='Ramdom text',
            price=0.05)

    def test_can_create_review_with_level_type_and_message(self):
        review = Review(
            reviewed_level_type=self.service,
            message='Ramdom text'
        )
        self.assertEqual(review.reviewed_level_type.level_type.level_type, 'Basic')

    def test_str_is_right_for_review_model(self):
        review = Review(
            reviewed_level_type=self.service,
            message='Ramdom text',
            author=self.user,
            date_of_contact='2020-01-01'
        )
        self.assertEqual(review.reviewed_level_type.level_type.level_type, 'Basic')
