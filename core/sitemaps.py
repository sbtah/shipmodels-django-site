from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from gallery.models import ImagePost, ImageGallery


class StaticViewSitemap(Sitemap):
    """Sitemap class for xml file for site."""

    def items(self):
        return [
            'home',
            'about',
            'cookies',
            'privacy-policy',
            'orders:order-create'
        ]

    def location(self, item):
        return reverse(item)


class ImagePostSitemap(Sitemap):

    def items(self):
        return ImagePost.objects.all()


class ImageGallerySitemap(Sitemap):

    def items(self):
        return ImageGallery.objects.all()
