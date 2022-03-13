import pytest
from django.urls import reverse
from banners.models import BannerImage, AboutBanner
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db


class TestBannerImage():
    """"Test BannerImage object."""

    def test_that_banner_image_can_be_created(self):
        """Test that BannerImage is created."""

        assert BannerImage.objects.all().count() == 0
        image = mixer.blend(BannerImage)
        assert BannerImage.objects.all().count() == 1

    def test_str_method_of_bannerimage(self):
        """Test that __str__ is properly generated."""

        banner_image = mixer.blend(BannerImage, tytuł='Test')
        assert str(banner_image) == f'BanerIMG:{banner_image.tytuł}'

    def test_get_filename_of_bannerimage(self):
        """Test that get_filename returns name of uploded file."""

        banner_image = mixer.blend(BannerImage, tytuł='Test')
        assert banner_image.get_filename() == 'default.jpg'
