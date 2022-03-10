import os
from PIL import Image as IMG
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.utils.text import slugify
from unidecode import unidecode
from gallery.utils import upload_to


# Model of Image object and it's methods.
class Image(models.Model):
    """Class for Image object."""

    tytuł = models.CharField(
        max_length=50,
        help_text=(_("Krótki tytuł")),
        unique=True,
        verbose_name=_('Tytuł')
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('Link')
    )
    obraz = models.ImageField(
        upload_to=upload_to("images/"),
        default="images/default.jpg",
        blank=True,
        null=True,
        verbose_name=_('Obraz')
    )
    obraz_opis = models.CharField(
        max_length=100,
        help_text=(_("Alt opis dla zdjęcia")),
        verbose_name=_('Obraz SEO opis')
    )
    dodano = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Dodano'))
    zaktualizowano = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Zaktualizowano'),
    )
    użyty = models.BooleanField(default=False, verbose_name=_('Użyty'))
    użyty_w_galerii = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_('Użyty w galerii:'),)

    class Meta:

        ordering = ('-dodano',)

    def get_absolute_url(self):
        return reverse('gallery:image-detail', kwargs={'slug': self.slug})

    def get_filename(self):
        return os.path.basename(self.obraz.name)

    def save(self, *args, **kwargs):
        """Custom save method that scales down images that customer will upload."""

        if self.obraz:
            super().save(*args, **kwargs)
            img = IMG.open(self.obraz.path)
            if img.height > 700 or img.width > 700:
                output_size = (700, 700)
                img.thumbnail(output_size)
                img.save(self.obraz.path)

    def __str__(self):
        return f'GalleryIMG:{self.tytuł}:{self.dodano.strftime("%b-%d-%Y")}'


# Model of Gallery object and it's methods.
class Gallery(models.Model):
    """Class for Gallery object."""

    tytuł = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_('Tytuł'),
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('Link'),
        help_text=_('Automatycznie generowany'),
    )
    opis_modelu = models.TextField(
        verbose_name=_('Opis modelu'),
        blank=True,
        null=True,
    )
    skala_modelu = models.CharField(
        max_length=50,
        verbose_name=_('Skala modelu'),
        blank=True,
        null=True,
    )
    długość_modelu = models.CharField(
        max_length=50,
        verbose_name=_('Długość modelu'),
        blank=True,
        null=True,
    )
    szerokość_modelu = models.CharField(
        max_length=50,
        verbose_name=_('Szerokość modelu'),
        blank=True,
        null=True,
    )
    wysokość_modelu = models.CharField(
        max_length=50,
        verbose_name=_('Wysokość modelu'),
        blank=True,
        null=True,
    )
    waga_modelu = models.CharField(
        max_length=50,
        verbose_name=_('Waga modelu'),
        blank=True,
        null=True,
    )
    główne_zdjęcie = models.OneToOneField(
        Image,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Główne zdjęcie'),
        related_name='main_image',
    )
    zdjęcia = models.ManyToManyField(
        Image,
        verbose_name=_('Zdjęcia'),
    )
    dodano = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Dodano'),
    )
    zaktualizowano = models.DateTimeField(
        auto_now=True, verbose_name=_('Zaktualizowano'))
    dodał = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('Dodał')
    )

    class Meta:

        ordering = ('-dodano',)
        verbose_name_plural = 'Galleries'

    def get_absolute_url(self):
        return reverse('gallery:gallery-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'Galeria:{self.tytuł} Dodał:{self.dodał.email}'


# Signals for all models.
@ receiver(post_save, sender=Image)
def create_slug_for_post(sender, instance, created, **kwargs):
    """Slugify signal for ImagePost object."""
    if created:
        instance.slug = slugify(unidecode(instance.tytuł))
        instance.save()


@ receiver(post_save, sender=Gallery)
def create_slug_for_gallery(sender, instance, created, **kwargs):
    """Slugify signal for ImageGallery object."""
    if created:
        instance.slug = slugify(unidecode(instance.tytuł))
        instance.save()


@ receiver(m2m_changed, sender=Gallery.zdjęcia.through)
def image_post_used(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        qs = kwargs.get('model').objects.filter(pk__in=kwargs.get('pk_set'))
        for item in qs:
            item.użyty = True
            item.użyty_w_galerii = str(instance.tytuł)
            item.save()

    elif action == 'post_remove':
        qs = kwargs.get('model').objects.filter(pk__in=kwargs.get('pk_set'))
        for item in qs:
            item.użyty = False
            item.użyty_w_galerii = None
            item.save()
