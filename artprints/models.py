"""
Database models for the Art Prints app
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    """
    Art Categories
    """
    categories = models.CharField(max_length=20)

    class Meta:
        """
        Display order
        """
        ordering = ('categories',)

    def __str__(self):
        """
        Display order
        """
        return self.categories


class ArtPrint(models.Model):
    """
    Database model for printed artworks
    """
    print_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    artist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='art_prints')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=False, null=False)
    artwork_image = CloudinaryField('image', null=False, blank=False)
    print_height = models.IntegerField(null=False, blank=False)
    print_width = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    print_run = models.IntegerField(null=False, blank=False)
    remaining_copies = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    likes = models.ManyToManyField(User, related_name='print_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        """
        To diplay the most recently
        uploaded artwork first
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        To display the print name
        instead of the model ID.
        """
        return self.print_name

    def number_of_likes(self):
        """
        To return total number of print likes
        """
        return self.likes.count()
