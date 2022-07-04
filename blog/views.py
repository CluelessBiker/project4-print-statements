"""
Functions for the view code,
"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import BlogPost
from .forms import CommentForm


def home_page(request):
    """
    View for home page.
    """
    return render(request, 'index.html')


# Class used from "I think therefore I blog" walkthrough.
class BlogPage(generic.ListView):
    """
    View for blog page.
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 5


# Class used from "I think therefore I blog" walkthrough.
class BlogPostPage(View):
    """
    To render the individual blog post
    as a singular web page to the browser.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Create a new URL path
        for each blog post
        """
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'blog-post.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked
                'comment_form': CommentForm()
            },
        )
