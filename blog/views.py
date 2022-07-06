"""
Functions for the view code,
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import BlogPost
from .forms import CommentForm


def home_page(request):
    """
    View for home page.
    """
    return render(request, 'index.html')


def about_page(request):
    """
    View for about page.
    """
    return render(request, 'about.html')


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
        for each blog post.
        Create a comments section on the page.
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
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Submit a new comment to a
        blog post.
        """
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'blog-post.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


# Class used from "I think therefore I blog" walkthrough.
class LikeBlogPost(View):
    """
    Allow a user to like a
    blog post submission
    """
    def post(self, request, slug):
        """
        Check for user.
        And like/unlike a post
        """
        post = get_object_or_404(BlogPost, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_post', args=[slug]))
