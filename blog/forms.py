"""
Comments form, allowing users to
comment on blog posts
"""
from .models import BlogComment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Which form fields should be populated
    to submit a comment
    """
    class Meta:
        model = BlogComment
        fields = ('body',)
