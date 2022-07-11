"""
URL paths to render each view to the browser.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('prints/', views.PrintsPage.as_view(), name='prints'),
    path('submitprint/', views.submit_art_print, name='submit_print'),
    path('<slug:slug>/', views.PrintDetails.as_view(), name='print_detail'),
    path('like/<slug:slug>', views.LikeArtPrint.as_view(), name='like_print'),
]
