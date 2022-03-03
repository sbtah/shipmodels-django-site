from django import forms
from orders.models import Order
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    """Modelform for Order object."""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['phone_number'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['model'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['comment'].widget.attrs.update(
            {'class': 'form__input form__label'})

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'email', 'model', 'comment',)
