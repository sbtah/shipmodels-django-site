from django.contrib import admin
from gallery.models import Image, Gallery
from gallery.forms import GalleryForm


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """Custom model admin that utilizes GalleryForm."""

    form = GalleryForm
    fields = (
        ('tytuł', ),
        'slug',
        'opis_modelu',
        'skala_modelu',
        'długość_modelu',
        'szerokość_modelu',
        'wysokość_modelu',
        'waga_modelu',
        'główne_zdjęcie',
        'zdjęcia',
        'dodał'
    )

    list_display = ('tytuł', 'dodano', 'główne_zdjęcie',)
    list_filter = ('tytuł', 'dodano', 'główne_zdjęcie',)
    ordering = ('-dodano',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Custom model admin for Image objects."""

    fields = (('tytuł', ), 'slug', 'obraz',
              'obraz_opis', 'użyty', 'użyty_w_galerii')

    list_display = ('tytuł', 'dodano', 'użyty', 'użyty_w_galerii')
    list_filter = ('tytuł', 'dodano', 'użyty',)
    ordering = ('-dodano',)
