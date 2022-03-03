from django import forms
from gallery.models import ImageGallery
from django.utils.translation import gettext_lazy as _


class ImageGalleryForm(forms.ModelForm):
    """Model form for ImageGallery object."""

    def clean_posts(self):
        """Custom clean """
        posts = self.cleaned_data['posts']
        if len(posts) > 9:
            raise forms.ValidationError(_('You can add maximum 9 images'))
        return posts

    class Meta:
        model = ImageGallery
        fields = ('title', 'posts')
