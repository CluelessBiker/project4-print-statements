"""
PYTHON TESTS FOR VIEWS
"""
from django.test import TestCase


# Test taken from "Hello Django"
class TestViews(TestCase):
    """
    Test views.
    """
    def test_prints_page(self):
        """
        Verify prints page loads
        """
        response = self.client.get('/art/prints', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prints.html')
