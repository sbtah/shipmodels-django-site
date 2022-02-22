from gallery.models import ImagePost
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

    def get_queryset(self):
        return get_object_or_404(ImagePost, slug=self.kwargs['slug'])


class ImageGalleryListView(generic.ListView):
    """Public ListView for ImageGallery objects."""

    model = ImagePost
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'
