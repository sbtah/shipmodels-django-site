from gallery.models import Gallery, Image
from django.views import generic


# Views for ImagePosts
class ImageListView(generic.ListView):
    """Public ListView for ImagePost objects."""

    model = Image
    template_name = 'gallery/image_list.html'


class ImageDetailView(generic.DetailView):
    """Public DetailView for ImagePost object."""

    model = Image
    template_name = 'gallery/image_detail.html'
    context_object_name = 'image'


# Views for ImageGalleries
class GalleryListView(generic.ListView):
    """Public ListView for ImageGallery objects."""

    model = Gallery
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'


class GalleryDetailView(generic.DetailView):
    """Public DetailView for ImageGallery object."""

    model = Gallery
    template_name = 'gallery/gallery_detail.html'
    context_object_name = 'gallery'
