"""
Functions for the view code
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import ArtPrint


class PrintsPage(generic.ListView):
    """
    View prints page.
    """
    model = ArtPrint
    queryset = ArtPrint.objects.filter(status=1).order_by('-created_on')
    template_name = 'prints.html'
    paginate_by = 12


class PrintDetails(View):
    """
    Render the individual print
    to the browser.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = ArtPrint.objects.filter(status=1)
        print = get_object_or_404(queryset, slug=slug)
        liked = False
        if print.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'print-details.html',
            {
                'print': print,
                'liked': liked
            }
        )


# Class used from "I think therefore I blog" walkthrough.
class LikeArtPrint(View):
    """
    Allow a user to like an
    art print submission
    """
    def post(self, request, slug):
        """
        Check for user.
        And like/unlike a post
        """
        print = get_object_or_404(ArtPrint, slug=slug)

        if print.likes.filter(id=request.user.id).exists():
            print.likes.remove(request.user)
        else:
            print.likes.add(request.user)

        return HttpResponseRedirect(reverse('print_detail', args=[slug]))
