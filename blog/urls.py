"""
URL paths to render each viw to the browser.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/', views.BlogPage.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogPostPage.as_view(), name='blog_post'),
    path('like/<slug:slug>', views.LikeBlogPost.as_view(), name='like_post'),
]
