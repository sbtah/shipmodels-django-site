import pytest
from django.urls import reverse
from gallery.models import ImagePost, ImageGallery
from orders.models import Order
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db


class TestImagePostModel():
    """Test cases for ImagePost object."""

    def test_image_can_be_created(self):
        """Test that ImagePost object is created"""
        assert ImagePost.objects.all().count() == 0
        image = mixer.blend(ImagePost)
        assert ImagePost.objects.all().count() == 1

    def test_str_method_of_image(self):
        """Test that __str__ is properly generated."""

        image = mixer.blend(ImagePost, tytuł='Test')
        assert str(
            image) == f'Obraz:Test Dodano:{image.dodano.strftime("%b-%d-%Y")}'

    def test_create_slug_for_image_signal(self):
        """Test that creating slug from title is working on save."""

        image = mixer.blend(ImagePost, tytuł='Testąt')
        assert image.slug == 'testat'

    def test_create_slug_for_image_must_be_unique(self):
        """Test that slug can only be saved with unique slug."""

        image = mixer.blend(ImagePost, tytuł='Testąt')
        with pytest.raises(Exception) as error:
            image_2 = mixer.blend(ImagePost, tytuł='Testąt')

    def test_absolute_url_of_created_image(self):
        """Test get_absolute_url() method of ImagePost objects."""

        image = mixer.blend(ImagePost, tytuł='Testąt')
        assert image.get_absolute_url() == reverse(
            'gallery:image-detail',
            args=[image.slug])


class TestImageGalleryModel():
    """Test cases for ImagePost object."""

    def test_gallery_can_be_created(self):
        """Test that ImagePost object is created"""
        assert ImageGallery.objects.all().count() == 0
        gallery = mixer.blend(ImageGallery)
        assert ImageGallery.objects.all().count() == 1

    def test_str_method_of_gallery(self, example_user):
        """Test that __str__ is properly generated."""

        user = example_user
        gallery = mixer.blend(ImageGallery, tytuł='Test',
                              dodał=user)
        assert str(gallery) == "Galeria:Test Dodał:test@test.com"

    def test_create_slug_for_gallery_signal(self):
        """Test that creating slug from title is working on save."""

        gallery = mixer.blend(ImageGallery, tytuł='Testąt')
        assert gallery.slug == 'testat'

    def test_create_slug_for_gallery_must_be_unique(self):
        """Test that slug can only be saved with unique slug."""

        gallery = mixer.blend(ImageGallery, tytuł='Testąt')
        with pytest.raises(Exception) as error:
            gallery_2 = mixer.blend(ImageGallery, tytuł='Testąt')

    def test_absolute_url_of_created_gallery(self):
        """Test get_absolute_url() method of ImageGallery objects."""

        gallery = mixer.blend(ImageGallery, tytuł='Testąt')
        assert gallery.get_absolute_url() == reverse(
            'gallery:gallery-detail',
            args=[gallery.slug])


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

        order = mixer.blend(Order, imię_i_nazwisko='Tester', model='Statek')
        assert str(
            order) == "Order ID:1, By:Tester, Model:Statek"

    def test_order_model_absolute_url(self):
        """Test absolute url method of Order model."""

        order = mixer.blend(Order)
        assert order.get_absolute_url() == reverse(
            'panel:order-detail',
            args=[order.id]
        )
