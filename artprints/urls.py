"""
URL paths to render each view to the browser.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('prints/', views.PrintsPage.as_view(), name='prints'),
    path('<slug:slug>/', views.PrintDetails.as_view(), name='print_detail'),
]
