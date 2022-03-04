from PIL import Image
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from unidecode import unidecode


class ImagePost(models.Model):
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
        upload_to="images/",
        default="default.jpg",
        blank=True,
        null=True,
        verbose_name=_('Obraz')
    )
    obraz_opis = models.CharField(
        max_length=100,
        help_text=(_("Alt Description for Photo")),
        verbose_name=_('Obraz opis')
    )
    dodano = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Dodano'))
    zaktualizowano = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Zaktualizowano'),
    )
    dodane_przez = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('Dodane przez')
    )

    class Meta:

        ordering = ('-dodano',)

    def get_absolute_url(self):
        return reverse('gallery:image-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Custom save method that scales down images that customer will upload."""

        if self.obraz:
            super().save(*args, **kwargs)
            img = Image.open(self.obraz.path)
            if img.height > 700 or img.width > 700:
                output_size = (700, 700)
                img.thumbnail(output_size)
                img.save(self.obraz.path)

    def __str__(self):
        return self.tytuł


class ImageGallery(models.Model):
    """Class for ImageGallery object."""

    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_('Title'),
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('Link'),
    )
    posts = models.ManyToManyField(
        ImagePost,
        verbose_name=_('Posts'),
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created'),
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('Created by')
    )

    class Meta:

        ordering = ('-created',)
        verbose_name_plural = 'ImageGalleries'

    def get_absolute_url(self):
        return reverse('gallery:gallery-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


@receiver(post_save, sender=ImagePost)
def create_slug_for_post(sender, instance, created, **kwargs):
    """Slugify signal for ImagePost object."""
    if created:
        instance.slug = slugify(unidecode(instance.tytuł))
        instance.save()


@receiver(post_save, sender=ImageGallery)
def create_slug_for_gallery(sender, instance, created, **kwargs):
    """Slugify signal for ImageGallery object."""
    if created:
        instance.slug = slugify(unidecode(instance.title))
        instance.save()
