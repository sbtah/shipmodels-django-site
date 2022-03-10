import os
from django.db import models
from django.urls import reverse
from PIL import Image as IMG
from django.utils.translation import gettext_lazy as _
from gallery.utils import upload_to


# Model of BannerImage object and it's methods.
class BannerImage(models.Model):
    """Class for BannerImage object."""

    tytuł = models.CharField(max_length=50, help_text=_('Tytuł'))
    obraz = models.ImageField(
        upload_to=upload_to("banners/"),
        default="banners/default.jpg",
        blank=True,
        null=True,
        verbose_name=_('Obraz baneru')
    )
    obraz_opis = models.CharField(
        max_length=100,
        help_text=(_("Alt opis dla zdjęcia")),
        verbose_name=_('Obraz SEO opis')
    )

    def get_absolute_url(self):
        return reverse('banners:bannerimage-detail', kwargs={'pk': self.id})

    def get_filename(self):
        return os.path.basename(self.obraz.name)

    def save(self, *args, **kwargs):
        """Custom save method that scales down images that customer will upload."""

        if self.obraz:
            super().save(*args, **kwargs)
            img = IMG.open(self.obraz.path)
            if img.height > 1600 or img.width > 1050:
                output_size = (1060, 1050)
                img.thumbnail(output_size)
                img.save(self.obraz.path)

    def __str__(self):
        return f'BanerIMG:{self.tytuł}'


# Model of Banner object and it's methods.
class Banner(models.Model):
    """Class for Banner object."""

    tytuł = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_('Tytuł'),
    )
    zdjęcia = models.ManyToManyField(
        BannerImage,
        verbose_name=_('Zdjęcia'),
    )

    def get_absolute_url(self):
        return reverse('banners:banner-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'Bannner:{self.tytuł}'

    class Meta:
        abstract = True


class AboutBanner(Banner):
    """Class for Banner displayed on About Us page."""

    is_active = models.BooleanField(default=False, verbose_name=_('Aktywny'))
