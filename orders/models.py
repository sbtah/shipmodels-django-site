from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Order(models.Model):
    """Class for Order object."""

    full_name = models.CharField(max_length=50, help_text=(_('Full name')))
    phone_number = models.DecimalField(
        max_digits=12, decimal_places=0, help_text=(_('Phone number')))
    email = models.EmailField(help_text=(_('Email address')))
    model = models.CharField(help_text=(_('Model')))
    comment = models.TextField(help_text=(_('Description')))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ('-created',)

    def get_absolute_url(self):
        """Return abosolute url to single object."""
        return reverse('orders:order-detail', kwargs={'pk': self.id})

    def __str__(self):
        return f"Order ID:{self.id}, By:{self.title}, Model:{self.model}"
