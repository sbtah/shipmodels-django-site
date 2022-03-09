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


class Image(models.Model):
    """Class for ImagePost object."""

    tytuł = models.CharField(
        max_length=25,
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
        verbose_name=_('Obraz opis')
    )
    dodano = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Dodano'))
    zaktualizowano = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Zaktualizowano'),
    )
    dodał = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('Dodał')
    )
    użyty = models.BooleanField(default=False, verbose_name=_('Użyty'))
    użyty_w_galerii = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_('Użyty w galerii:'),)

    class Meta:

        ordering = ('-dodano',)

    def get_absolute_url(self):
        return reverse('gallery:image-detail', kwargs={'slug': self.slug})

    def get_image_filename(self):
        if not self.obraz:
            return ""
        file_path = self.obraz.name
        return os.path.basename(file_path)

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
        return f'Obraz:{self.tytuł} Dodano:{self.dodano.strftime("%b-%d-%Y")}'


class Gallery(models.Model):
    """Class for ImageGallery object."""

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
        limit_choices_to={'użyty': False},
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


@receiver(post_save, sender=Image)
def create_slug_for_post(sender, instance, created, **kwargs):
    """Slugify signal for ImagePost object."""
    if created:
        instance.slug = slugify(unidecode(instance.tytuł))
        instance.save()


@receiver(post_save, sender=Gallery)
def create_slug_for_gallery(sender, instance, created, **kwargs):
    """Slugify signal for ImageGallery object."""
    if created:
        instance.slug = slugify(unidecode(instance.tytuł))
        instance.save()


@receiver(m2m_changed, sender=Gallery.zdjęcia.through)
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
