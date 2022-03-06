from gallery.models import ImageGallery, ImagePost
from django.views import generic


# Views for ImagePosts
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


# Views for ImageGalleries
class ImageGalleryListView(generic.ListView):
    """Public ListView for ImageGallery objects."""

    model = ImageGallery
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'


class ImageGalleryDetailView(generic.DetailView):
    """Public DetailView for ImageGallery object."""

    model = ImageGallery
    template_name = 'gallery/gallery_detail.html'
    context_object_name = 'gallery'
