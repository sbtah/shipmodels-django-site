from django import forms
from orders.models import Order
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class OrderForm(forms.ModelForm):
    """Modelform for Order object."""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['imię_i_nazwisko'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['numer_telefonu'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['model'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['komentarz'].widget.attrs.update(
            {'class': 'form__input form__label'})

    class Meta:
        model = Order
        fields = ('imię_i_nazwisko', 'numer_telefonu',
                  'email', 'model', 'komentarz',)

    def clean_numer_telefonu(self):
        """Custom phone number clean"""
        phone_number = self.cleaned_data['numer_telefonu']
        if int(phone_number) < 0:
            raise forms.ValidationError(
                _('Błędny numer telefonu'))

        return phone_number

    def clean_imię_i_nazwisko(self):
        """Custom full name clean"""

        imię_i_nazwisko = self.cleaned_data['imię_i_nazwisko']
        if len(imię_i_nazwisko) < 2:
            raise ValidationError(
                _('Podane Imię i Nazwisko jest za krótkie'),
                params={'value': imię_i_nazwisko}
            )

        elif not all(x.isalpha() or x.isspace() for x in imię_i_nazwisko):
            raise ValidationError(
                _('Imię i Nazwisko może się składać tylko z liter'),
                params={'value': imię_i_nazwisko}
            )

        return imię_i_nazwisko
