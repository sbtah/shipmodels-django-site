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

    title = models.CharField(
        max_length=25,
        help_text=(_("Short Title")),
        unique=True
    )
    slug = models.CharField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(
        upload_to="images/",
        default="default.jpg",
        blank=True,
        null=True
    )
    image_description = models.CharField(
        max_length=100,
        help_text=(_("Alt Description for Photo"))
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.CASCADE)

    class Meta:

        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('gallery:image-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Custom save method that scales down images that customer will upload."""

        if self.image:
            super().save(*args, **kwargs)
            img = Image.open(self.image.path)
            if img.height > 700 or img.width > 700:
                output_size = (700, 700)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    """Class for ImageGallery object."""

    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )
    gallery = models.ManyToManyField(ImagePost)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.CASCADE)

    class Meta:

        ordering = ('-created',)
        verbose_name_plural = 'ImageGalleries'

    def get_absolute_url(self):
        return reverse('galeria:gallery', kwargs={'slug': self.slug})

    # TD: Slug on save POLISH slug!
    def __str__(self):
        return self.title


@receiver(post_save, sender=ImagePost)
def create_slug_for_post(sender, instance, created, **kwargs):
    """Slugify signal for ImagePost object."""
    if created:
        instance.slug = slugify(unidecode(instance.title))
        instance.save()


@receiver(post_save, sender=ImageGallery)
def create_slug_for_gallery(sender, instance, created, **kwargs):
    """Slugify signal for ImageGallery object."""
    if created:
        instance.slug = slugify(unidecode(instance.title))
        instance.save()
