"""
Functions for the view code
"""
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import ArtPrint
from .forms import SubmitPrintForm


class PrintsPage(generic.ListView):
    """
    View prints page.
    """
    model = ArtPrint
    queryset = ArtPrint.objects.filter(status=1).order_by('-created_on')
    template_name = 'prints.html'
    paginate_by = 12


def submit_art_print(request):
    """
    View for print submission page.
    """
    if request.method == 'POST':
        # breakpoint()
        submission_form = SubmitPrintForm(request.POST, request.FILES)
        if submission_form.is_valid():
            submission_form.instance.artist = request.user
            submission_form.save()
            return redirect('prints')
        else:
            print("ERROR")
            print(submission_form.errors)
            submission_form = SubmitPrintForm()

    return render(
        request,
        'submit-print.html',
        {
            'submission_form': SubmitPrintForm(),
        },
    )


# class PrintDetails(View):
#     """
#     Render the individual print
#     to the browser.
#     """
#     def get(self, request, slug, *args, **kwargs):
#         """
#         Obtain print & check for likes.
#         """
#         queryset = ArtPrint.objects.filter(status=1)
#         prints = get_object_or_404(queryset, slug=slug)
#         liked = False
#         if prints.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             'print-details.html',
#             {
#                 'prints': prints,
#                 'liked': liked,
#             }
#         )
class PrintDetails(View):
    """
    Render the individual print
    to the browser.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Obtain print & check for likes.
        """
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
        prints = get_object_or_404(ArtPrint, slug=slug)

        if prints.likes.filter(id=request.user.id).exists():
            prints.likes.remove(request.user)
        else:
            prints.likes.add(request.user)

        return HttpResponseRedirect(reverse('print_detail', args=[slug]))
