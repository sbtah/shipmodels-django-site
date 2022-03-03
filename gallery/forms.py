from django import forms
from gallery.models import ImageGallery
from django.utils.translation import gettext_lazy as _


class ImageGalleryForm(forms.ModelForm):
    """Model form for ImageGallery object."""

    def __init__(self, *args, **kwargs):
        """Custom __init__ that applies css classes to form style."""
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form__input form__label'})
        self.fields['posts'].widget.attrs.update(
            {'class': 'form__input form__label'})

    def clean_posts(self):
        """Custom clean """
        posts = self.cleaned_data['posts']
        if len(posts) > 9:
            raise forms.ValidationError(_('You can add maximum 9 images'))
        return posts

    class Meta:
        model = ImageGallery
        fields = ('title', 'posts')
