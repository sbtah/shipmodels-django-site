from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """Sitemap class for xml file for site."""

    def items(self):
        return ['home', 'about', ]

    def location(self, item):
        return reverse(item)
