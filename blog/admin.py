"""
Providing access to the pre-installed
admin panel provided by django
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, BlogComment


# Class used from "I think therefore I blog" walkthrough.
@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Making the summernote text editor field
    availble in the BlogPost admin panel
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


# Class used from "I think therefore I blog" walkthrough.
@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    """
    Providing admin access to moderate
    submitted comments
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Function to approve pending
        user comments on blog posts
        """
        queryset.update(approved=True)
