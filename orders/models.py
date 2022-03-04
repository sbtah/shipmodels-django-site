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
            _('Phone number should have only positive value'),
            params={'value': val}
        )


class Order(models.Model):
    """Class for Order object."""

    full_name = models.CharField(max_length=50)
    phone_number = models.DecimalField(
        max_digits=12, decimal_places=0, validators=[phone_number_validator])
    email = models.EmailField()
    model = models.CharField(max_length=50)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ('-created',)

    def get_absolute_url(self):
        """Return abosolute url to single object."""
        return reverse('panel:order-detail', kwargs={'pk': self.id})

    def __str__(self):
        return f"Order ID:{self.id}, By:{self.full_name}, Model:{self.model}"
