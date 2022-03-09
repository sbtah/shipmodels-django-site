from tkinter import Image
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

    # def get_context_data(self, **kwargs):
    #     context = super(ImageGalleryDetailView, self).get_context_data(
    #         **kwargs)  # get the default context data
    #     context['voted_links'] = Image.objects.filter(
    #         imagegallery__in=self)  # add extra field to the context
    #     return context


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
