import pytest
from django.urls import reverse
from banners.models import Banner, BannerImage, AboutBanner
from django.core.exceptions import ValidationError
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


class TestAboutBanner():
    """Test Banner object."""

    def test_that_aboutbanner_can_be_created(self):
        """Test that AboutBanner object is created."""

        assert AboutBanner.objects.all().count() == 0
        about_banner = mixer.blend(AboutBanner)
        assert AboutBanner.objects.all().count() == 1

    def test_str_method_of_aboutbanner(self):
        """Test that __str__ is properly generated."""

        about_banner = mixer.blend(AboutBanner, tytuł='test', is_active=True)
        about_banner2 = mixer.blend(
            AboutBanner, tytuł='test2', is_active=False)
        assert str(
            about_banner) == "Bannner:test Status:AKTYWNY"
        assert str(
            about_banner2) == "Bannner:test2 Status:NIEAKTYWNY"

    def test_is_active_raises_validation_error(self):
        """Test that there can be only one Banner with status is_avtive=True"""

        with pytest.raises(ValidationError) as error:
            about_banner = mixer.blend(
                AboutBanner, tytuł='test', is_active=True)
            # Since validators are run only on forms I have to check it this way!
            AboutBanner.is_active.field.run_validators(value=True)
