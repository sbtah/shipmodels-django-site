from gallery.models import ImagePost
from django.views import generic
from django.urls import reverse, reverse_lazy


class ImagePostListView(generic.ListView):
    """ListView for ImagePost objects."""

    model = ImagePost
    template_name = 'gallery/image_list.html'
    context_object_name = 'images'


class ImageGalleryListView(generic.ListView):
    """ListView for ImageGallery objects."""

    model = ImagePost
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'
