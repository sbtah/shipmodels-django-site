from django.contrib import admin
from gallery.models import Image, Gallery
from gallery.forms import GalleryForm


class GalleryAdmin(admin.ModelAdmin):
    """Custom model admin that utilizes GalleryForm."""
    form = GalleryForm


admin.site.register(Image)
admin.site.register(Gallery, GalleryAdmin)
