"""
Providing access to Art Print
in the django admin panel
"""
from django.contrib import admin
from .models import ArtPrint


@admin.register(ArtPrint)
class PrintAdmin(admin.ModelAdmin):
    prepoulated_fields = {'slug': ('print_name',)}
    list_display = ('artist', 'status', 'created_on')
    list_filter = ('artist', 'created_on')
    search_fields = ['print_name', 'artist']
