from django.test import SimpleTestCase
from django.urls import reverse


class HelloWorldTests(SimpleTestCase):
    def test_home_page_shows_hello_world(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, world!')
