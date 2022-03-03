from gallery.models import ImageGallery, ImagePost
from django.views import generic
from django.shortcuts import get_object_or_404


class ImagePostListView(generic.ListView):
    """Public ListView for ImagePost objects."""

    model = ImagePost
    template_name = 'gallery/image_list.html'
    context_object_name = 'images'


class ImagePostDetailView(generic.DetailView):
    """Public DetailView for ImagePost object."""

    model = ImagePost
    template_name = 'gallery/image_detail.html'
    context_object_name = 'image'


class ImageGalleryListView(generic.ListView):
    """Public ListView for ImageGallery objects."""

    model = ImageGallery
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'
