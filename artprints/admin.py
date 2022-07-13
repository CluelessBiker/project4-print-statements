"""
Providing access to Art Print
in the django admin panel
"""
from django.contrib import admin
from .models import ArtPrint, Category


@admin.register(ArtPrint)
class PrintAdmin(admin.ModelAdmin):
    """
    Class to define how the information
    is displayed in the admin panel
    """
    prepopulated_fields = {'slug': ('print_name',)}
    list_display = ('print_name', 'artist', 'status', 'created_on')
    list_filter = ('artist', 'created_on')
    search_fields = ['print_name', 'artist']
    actions = ['publish_print']

    def publish_print(self, request, queryset):
        """
        Function to approve pending
        art posts.
        """
        queryset.update(status=1)


admin.site.register(Category)
