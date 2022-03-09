from django import forms
from django.db.models import Q
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
        self.fields['dodał'].widget.attrs.update(
            {'class': 'form__input form__label'})

    class Meta:
        model = Image
        fields = ('tytuł', 'slug', 'obraz', 'obraz_opis', 'dodał')


class GalleryForm(forms.ModelForm):
    """Model form for ImageGallery object."""

    def __init__(self, *args, ** kwargs):
        """Custom __init__ that applies css classes to form style."""

        super(GalleryForm, self).__init__(*args, **kwargs)
        # print(args, kwargs)
        # self.fields['główne_zdjęcie'].queryset = ImagePost.objects.filter(
        #     Q(imagegallery__isnull=True) & Q(imagegallery__id=kwargs.get('instance')))
        # self.fields['zdjęcia'].queryset = ImagePost.objects.filter(
        #     Q(imagegallery__isnull=True) & Q(imagegallery__id=kwargs.get('instance')))

        self.fields['tytuł'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['główne_zdjęcie'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['zdjęcia'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['dodał'].widget.attrs.update(
            {'class': 'form__input form__label'})

    def clean_posts(self):
        """Custom clean """
        posts = self.cleaned_data['zdjęcia']
        if len(posts) > 9:
            raise forms.ValidationError(
                _('Możesz dodać tylko 9 zdjęć do galerii.'))
        return posts

    class Meta:
        model = Gallery
        fields = ('tytuł', 'slug', 'główne_zdjęcie', 'zdjęcia', 'dodał')
