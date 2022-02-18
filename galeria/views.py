from galeria.models import ImagePost
from django.views import generic
from django.urls import reverse, reverse_lazy


class ImagePostListView(generic.ListView):
    """ListView for ImagePost object."""

    model = ImagePost
    template_name = 'galeria/gallery_post_list.html'
