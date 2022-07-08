"""
URL paths to render each view to the browser.
"""
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.artprints, name='artprints'),
    path('prints/', views.PrintsPage.as_view(), name='prints'),
]
