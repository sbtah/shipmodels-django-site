from django import forms
from orders.models import Order
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    """Modelform for Order object."""

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'email', 'model', 'comment',)
