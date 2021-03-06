from django.db import models
from core.validators import fullname_validator, phone_number_validator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    """Class for Order object."""

    imię_i_nazwisko = models.CharField(
        max_length=50,
        verbose_name=_('Imię i Nazwisko'),
        validators=[fullname_validator]
    )
    numer_telefonu = models.CharField(
        max_length=20,
        verbose_name=_('Numer telefonu'),
        validators=[phone_number_validator],
    )
    email = models.EmailField(verbose_name=_('Email'))
    model = models.CharField(max_length=50, verbose_name=_('Model'))
    komentarz = models.TextField(
        blank=True, null=True, verbose_name=_('Komentarz'))
    dodano = models.DateTimeField(auto_now_add=True, verbose_name=_('Dodano'))
    zaktualizowano = models.DateTimeField(
        auto_now=True, verbose_name=_('Zaktualizowano'))

    class Meta:

        ordering = ('-dodano',)

    def get_absolute_url(self):
        """Return abosolute url to single object."""
        return reverse('panel:order-detail', kwargs={'pk': self.id})

    def __str__(self):
        return f"Order ID:{self.id}, By:{self.imię_i_nazwisko}, Model:{self.model}"


# Implement singal that will save an email when order is placed by a user.
