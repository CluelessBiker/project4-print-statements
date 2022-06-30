from django.contrib import admin
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Making the summernote text editor field
    availble in the BlogPost admin panel
    """
    summernote_fields = ('content')
