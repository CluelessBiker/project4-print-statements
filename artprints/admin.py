"""
Providing access to Art Print
in the django admin panel
"""
from django.contrib import admin
from .models import ArtPrint, Category


@admin.register(ArtPrint)
class PrintAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('print_name',)}
    list_display = ('print_name', 'artist', 'status', 'created_on')
    list_filter = ('artist', 'created_on')
    search_fields = ['print_name', 'artist']


admin.site.register(Category)
