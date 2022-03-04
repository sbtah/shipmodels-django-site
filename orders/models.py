from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model
# TD : User have to be logged in to create an Order.


def phone_number_validator(val):
    """Custom validator for orders's phone_number"""

    if val < 0:
        raise ValidationError(
            _('Błędny numer telefonu'),
            params={'value': val}
        )


class Order(models.Model):
    """Class for Order object."""

    imię_i_nazwisko = models.CharField(
        max_length=50, verbose_name=_('Imię i Nazwisko'))
    numer_telefonu = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        validators=[phone_number_validator],
        verbose_name=_('Numer telefonu')
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
