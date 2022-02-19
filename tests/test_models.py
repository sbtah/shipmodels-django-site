import pytest
from galeria.models import ImagePost
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from django.contrib.auth import get_user_model


pytestmark = pytest.mark.django_db


class TestImagePostModel():
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

    def test(self):
        pass


class TestUserModel():
    """Test cases for User object."""

    def test_create_user_with_email_succesful(self):
        """Test creating new user with email."""

        assert get_user_model().objects.all().count() == 0
        email = 'test@test.com'
        password = 'testpass123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        assert user.email == 'test@test.com'
        assert user.check_password(password) == True
