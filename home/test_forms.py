from django.test import TestCase
from .forms import ContactUsForm

# Create your tests here.


class TestHomeForms(TestCase):

    def test_form_can_be_submitted_with_all_fields_filled(self):
        form = ContactUsForm({
            'email': 'email@email.com',
            'message': 'test message',
        })

        self.assertTrue(form.is_valid())

    def test_form_cannot_be_submitted_if_email_field_blank(self):
        form = ContactUsForm({
            'email': '',
            'message': 'test message',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_form_cannot_be_submitted_if_message_field_blank(self):
        form = ContactUsForm({
            'email': 'email@email.com',
            'message': '',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_valid_email_included_in_email_field(self):
        form = ContactUsForm({
            'email': 'emailemail.com',
            'message': 'test message',
        })

        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactUsForm()

        self.assertEqual(form.Meta.fields, ['email', 'message'])
