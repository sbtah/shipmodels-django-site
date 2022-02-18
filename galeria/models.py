from PIL import Image
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse


class ImagePost(models.Model):
    """Class for ImagePost object."""

    title = models.CharField(max_length=25, help_text=(_("Short Title")))
    slug = models.CharField(max_length=25, unique=True)
    image = models.ImageField(
        upload_to="images/", default="default.jpg", blank=True, null=True)
    image_description = models.CharField(
        max_length=100, help_text=(_("Alt Description for Photo")))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.CASCADE)

    class Meta:

        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('galeria:image', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.image:
            super().save(*args, **kwargs)
            img = Image.open(self.image.path)
            if img.height > 700 or img.width > 700:
                output_size = (700, 700)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title
