from django.test import TestCase
from django.urls import reverse
from ..models import Contact


class IndexViewTests(TestCase):

    def test_index_view_uses_correct_template(self):
        url = reverse('portfolio:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_index_view_form_in_context(self):
        url = reverse('portfolio:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_index_view_url_accessible_by_name(self):
        url = reverse('portfolio:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_view_url_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_view_redirect_correct_url(self):
        response = self.client.post('/', {'name': 'test', 'email': 'test@example.com', 'message': 'message'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('portfolio:index'))


