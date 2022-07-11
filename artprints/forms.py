"""
Generate a form to allow signed-in users 
to submit new artworks.
"""
from django import forms
from .models import ArtPrint


class SubmitPrintForm(forms.ModelForm):
    """
    Art submission form
    """
    class Meta:
        """
        Generate which fields should be displayed.
        """
        model = ArtPrint
        fields = (
            'print_name',
            'description',
            'category',
            'artwork_image',
            'print_height',
            'print_width',
            'print_run',
            'remaining_copies',
            'price',
        )
        label = {
            'print_name': 'Title',
            'description': 'Description',
            'category': 'Category',
            'artwork_image': 'Select image',
            'print_height': 'Print height (in cm)',
            'print_width': 'Print width (in cm)',
            'print_run': "Number of available copies",
            'remaining_copies': "How many copies remain",
            'price': 'Price in Euros',
        }
