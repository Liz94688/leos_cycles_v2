from django.test import TestCase
from .forms import ReviewForm
from services.models import Level, Services


class TestReviewForm(TestCase):

    def test_form_can_be_submitted_with_all_the_fields_filled(self):

        test_reviewed_level_type = Level.objects.create(level_type='Basic')

        service = Services.objects.create(
            level_type=test_reviewed_level_type,
            description='Ramdom text',
            price=0.05)

        form = ReviewForm(data={'reviewed_level_type': service, 'message': 'random text'})
        self.assertTrue(form.is_valid())

    def test_form_cannot_be_submitted_without_level_type(self):
        form = ReviewForm({'reviewed_level_type': '', 'message': 'random text'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['reviewed_level_type'], [u'This field is required.'])

    def test_form_cannot_be_submitted_without_message(self):
        form = ReviewForm({'reviewed_level_type': 'level', 'message': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['message'], [u'This field is required.'])
