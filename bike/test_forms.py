from django.test import TestCase
from .forms import CreateBikeForm


class TestReviewForm(TestCase):

    def test_form_can_be_submitted_with_all_the_fields_filled(self):
        form = CreateBikeForm({'bike_type': 'type', \
            'frame_type': 'frame', 'handlebar_type': 'handlebar', \
                'wheel_size': '0', 'owner_description': 'random notes', \
                    'age': '0'})
        self.assertTrue(form.is_valid())

    def test_form_cannot_be_submitted_without_bike_type(self):
        form = CreateBikeForm({'bike_type': '', \
            'frame_type': 'frame', 'handlebar_type': 'handlebar', \
                'wheel_size': '0', 'owner_description': 'random notes', \
                    'age': '0'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['bike_type'], [u'This field is required.'])

    def test_form_cannot_be_submitted_without_frame_type(self):
        form = CreateBikeForm({'bike_type': 'type', \
            'frame_type': '', 'handlebar_type': 'handlebar', \
                'wheel_size': '0', 'owner_description': 'random notes', \
                    'age': '0'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['frame_type'], [u'This field is required.'])

    def test_form_cannot_be_submitted_without_handlebar_type(self):
        form = CreateBikeForm({'bike_type': 'type', \
            'frame_type': 'frame', 'handlebar_type': '', \
                'wheel_size': '0', 'owner_description': 'random notes', \
                    'age': '0'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['handlebar_type'], [u'This field is required.'])

    def test_form_cannot_be_submitted_without_wheel_size(self):
        form = CreateBikeForm({'bike_type': 'type', \
            'frame_type': 'frame', 'handlebar_type': 'handlebar', \
                'wheel_size': '', 'owner_description': 'random notes', \
                    'age': '0'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['wheel_size'], [u'This field is required.'])

    def test_form_cannot_be_submitted_without_owner_description(self):
        form = CreateBikeForm({'bike_type': 'type', \
            'frame_type': 'frame', 'handlebar_type': 'handlebar', \
                'wheel_size': '0', 'owner_description': '', \
                    'age': '0'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['owner_description'], [u'This field is required.'])

    def test_form_cannot_be_submitted_without_age(self):
        form = CreateBikeForm({'bike_type': 'type', \
            'frame_type': 'frame', 'handlebar_type': 'handlebar', \
                'wheel_size': '0', 'owner_description': 'random notes', \
                    'age': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['age'], [u'This field is required.'])

