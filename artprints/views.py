"""
Functions for the view code
"""
from django.shortcuts import render
from django.views import generic, View
from .models import ArtPrint


class PrintsPage(generic.ListView):
    """
    View prints page.
    """
    model = ArtPrint
    queryset = ArtPrint.objects.filter(status=1).order_by('-created_on')
    template_name = 'prints.html'
    paginate_by = 10
