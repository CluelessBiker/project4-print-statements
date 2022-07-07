"""
Providing access to Art Print
in the django admin panel
"""
from django.contrib import admin
from .models import ArtPrint


admin.site.register(ArtPrint)
