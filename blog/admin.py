from django.contrib import admin
from .models import BlogPost, BlogComments
from django_summernote.admin import SummernoteModelAdmin


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
@admin.register(BlogComments)
class CommentAdmin(admin.ModelAdmin):
    """
    Providing admin access to moderate
    submitted comments
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']