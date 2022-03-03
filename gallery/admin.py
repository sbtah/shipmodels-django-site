from django.contrib import admin
from gallery.models import ImagePost, ImageGallery
from gallery.forms import ImageGalleryForm


class ImageGalleryAdmin(admin.ModelAdmin):
    """Custom model admin that utilizes ImageGalleryForm."""
    form = ImageGalleryForm


admin.site.register(ImagePost)
admin.site.register(ImageGallery, ImageGalleryAdmin)
