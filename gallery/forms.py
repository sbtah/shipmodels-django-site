from django import forms
from gallery.models import Gallery, Image
from django.utils.translation import gettext_lazy as _


class ImageForm(forms.ModelForm):
    """Model form for ImagePost objects."""

    def __init__(self, *args, **kwargs):
        """Custom __init__ that applies css classes to form style."""

        super().__init__(*args, **kwargs)
        self.fields['tytuł'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['obraz'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['obraz_opis'].widget.attrs.update(
            {'class': 'form__input form__label'})

    class Meta:
        model = Image
        fields = ('tytuł', 'slug', 'obraz', 'obraz_opis',)


class GalleryForm(forms.ModelForm):
    """Model form for ImageGallery object."""

    def __init__(self, *args, ** kwargs):
        """Custom __init__ that applies css classes to form style."""

        super().__init__(*args, **kwargs)
        self.fields['tytuł'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['opis_modelu'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['skala_modelu'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['długość_modelu'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['szerokość_modelu'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['wysokość_modelu'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['waga_modelu'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['główne_zdjęcie'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['zdjęcia'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['dodał'].widget.attrs.update(
            {'class': 'form__input form__label'})

    class Meta:
        model = Gallery
        fields = (
            'tytuł',
            'slug',
            'opis_modelu',
            'skala_modelu',
            'długość_modelu',
            'szerokość_modelu',
            'wysokość_modelu',
            'waga_modelu',
            'główne_zdjęcie',
            'zdjęcia',
            'dodał'
        )

    def clean_zdjęcia(self):
        """Custom clean method that limits number of images in Gallery."""

        zdjęcia = self.cleaned_data['zdjęcia']
        if len(zdjęcia) > 8:
            raise forms.ValidationError(
                _('Możesz dodać tylko 8 zdjęć do galerii.'))

        return zdjęcia
