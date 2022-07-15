"""
PYTHON TESTS FOR FORMS
"""
from django.test import TestCase
from .forms import SubmitPrintForm


# Test taken from "Hello Django"
class TestSubmitPrintForm(TestCase):
    """
    Tests for Submit Print form.
    """
    def test_print_name_required(self):
        """
        Verify print name is required
        """
        form = SubmitPrintForm({'print_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('print_name', form.errors.keys())
        self.assertEqual(
            form.errors['print_name'][0], 'This field is required.')
