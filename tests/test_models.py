import pytest
from galeria.models import ImagePost
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db


class TestImagePost():
    """Test cases for ImagePost object."""

    def test_model_can_be_created(self):
        """Test that ImagePost object is created"""
        assert ImagePost.objects.all().count() == 0
        image = mixer.blend(ImagePost)
        assert ImagePost.objects.all().count() == 1

    def test_str_method_of_model(self):
        """Test that __str__ is properly generated."""

        image = mixer.blend(ImagePost, title='Test')
        assert str(image) == "Test"

    def test_user_is_assigned(self):
        """Test that crated_by field is properly linked to user."""

        pass
