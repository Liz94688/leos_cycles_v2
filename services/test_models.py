from django.test import TestCase
from .models import Services, Level

'''
I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
'''


class TestServiceModels(TestCase):

    def setUp(self):

        test_level_type = Level.objects.create(level_type='Basic')

        self.service = Services.objects.create(
            level_type=test_level_type,
            description='Ramdom mesage',
            price=0.05)

    def test_can_create_service(self):
        service = Services(
            level_type=self.service.level_type,
            description='Random message',
            price=0.05
        )

        self.assertEqual(service.level_type.level_type, 'Basic')
