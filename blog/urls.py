from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home'),
    # path('blog/', views.BlogPage.as_view(), name='blog'),
    path('blog/', views.BlogPage, name='blog'),
]