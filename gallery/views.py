from gallery.models import ImagePost
from django.views import generic


class ImagePostListView(generic.ListView):
    """Public ListView for ImagePost objects."""

    model = ImagePost
    template_name = 'gallery/image_list.html'
    context_object_name = 'images'


class ImageGalleryListView(generic.ListView):
    """Public ListView for ImageGallery objects."""

    model = ImagePost
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'
