from django import forms
from gallery.models import ImageGallery, ImagePost
from django.utils.translation import gettext_lazy as _


class ImageGalleryForm(forms.ModelForm):
    """Model form for ImageGallery object."""

    def __init__(self, *args, **kwargs):
        """Custom __init__ that applies css classes to form style."""

        super().__init__(*args, **kwargs)
        self.fields['tytuł'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['slug'].widget.attrs.update(
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
        model = ImageGallery
        fields = ('tytuł', 'slug', 'zdjęcia', 'dodał')
