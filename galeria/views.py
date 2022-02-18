from galeria.models import ImagePost
from django.views import generic
from django.urls import reverse, reverse_lazy


class ImagePostListView(generic.ListView):
    """ListView for ImagePost objects."""

    model = ImagePost
    template_name = 'galeria/post_list.html'
    context_object_name = 'images'


class ImageGalleryListView(generic.ListView):
    """ListView for ImageGallery objects."""

    model = ImagePost
    template_name = 'galeria/galleries_list.html'
    context_object_name = 'galleries'
