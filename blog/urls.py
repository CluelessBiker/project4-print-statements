from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('blog/', views.BlogPage.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogPostPage.as_view(), name='blog_post'),
]