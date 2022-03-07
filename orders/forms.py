from django import forms
from orders.models import Order
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    """Modelform for Order object."""

    def clean_phone_number(self):
        """Custom clean """
        phone_number = self.cleaned_data['numer_telefonu']
        if phone_number < 0:
            raise forms.ValidationError(
                _('Błędny numer telefonu'))
        return phone_number

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
