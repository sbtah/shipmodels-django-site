
import pytest
from django.urls import reverse
from gallery.models import ImagePost, ImageGallery
from orders.models import Order
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer


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

    def test_new_user_email_normalized(self):
        """Test that email for new user is normalized."""

        email = 'test@TEST.com'
        password = 'testpass123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        assert user.email == email.lower()

    def test_new_user_with_invalid_email(self):
        """Test creating user with no email raises an error."""

        with pytest.raises(Exception) as error:
            get_user_model().objects.create_user('', 'test123!')

    def test_create_super_user(self):
        """Test creating new super user."""

        assert get_user_model().objects.filter(is_superuser=True).exists() == False
        email = 'admin@admin.com'
        password = 'testpass123!'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )
        assert user.is_superuser == True
        assert user.is_staff == True

    def test_create_user_with_email_already_used(self):
        """Test that creation user with used email raises an exception."""

        user_1 = get_user_model().objects.create_user(
            email='test@test.com',
            password='testpass123',
        )
        with pytest.raises(Exception) as error:
            get_user_model().objects.create_user(
                email='test@test.com',
                password='testpass123',
            )


class TestOrderModel():
    """Test Cases for Order object."""

    def test_order_can_be_created(self):
        """Test that Order object can be created."""

        assert Order.objects.all().count() == 0
        order = mixer.blend(Order)
        assert Order.objects.all().count() == 1

    def test_str_method_of_order(self):
        """Test that __str__ is properly generated."""

        order = mixer.blend(Order, full_name='Tester', model='Statek')
        assert str(
            order) == "Order ID:1, By:Tester, Model:Statek"

    # def test_order_model_absolute_url(self):
    #     """Test absolute url method of Order model."""

    #     order = mixer.blend(Order)
    #     assert order.get_absolute_url() != reverse(
    #         'orders:order-detail',
    #         args=[order.id]
    #     )
