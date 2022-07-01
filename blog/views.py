"""
Functions for the view code,
"""
from django.shortcuts import render
from django.views import generic
from .models import BlogPost


# Class used from "I think therefore I blog" walkthrough.
class BlogPage(generic.ListView):
    """
    View for blog page.
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 5
