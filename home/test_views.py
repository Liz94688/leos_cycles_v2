from django.test import TestCase, Client

"""

I found out about testing tools and the Test Client from Django documentation:
https://docs.djangoproject.com/en/3.1/topics/testing/tools/

"""

c = Client()


class TestHomeViews(TestCase):

    def test_get_index_page(self):
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_about_page(self):
        response = c.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_get_contact_page(self):
        response = c.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')
