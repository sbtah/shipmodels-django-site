import pytest
from orders.models import Order
from orders.forms import OrderForm
from gallery.models import Image, Gallery
from gallery.forms import ImageForm, GalleryForm


pytestmark = pytest.mark.django_db


class TestOrderForm():
    """Test case for OrderForm."""

    def test_order_form_object_created(self):
        """Test that object is created through form."""

        order_data = {
            'imię_i_nazwisko': 'Test Tester',
            'numer_telefonu': '712712712',
            'email': 'test@test.com',
            'model': 'Statek',
            'komentarz': 'Do it now!',
        }

        form = OrderForm(data=order_data)
        assert form.is_valid()
        assert Order.objects.all().count() == 0
        form.is_valid()
        form.save()
        assert Order.objects.all().count() == 1
        assert Order.objects.filter(
            imię_i_nazwisko='Test Tester').exists() == True

    def test_order_form_clean_phone_number(self):
        """Test that data cannot be saved with bad phone number"""

        order_data = {
            'imię_i_nazwisko': 'Test Tester',
            'numer_telefonu': -1,
            'email': 'test@test.com',
            'model': 'Statek',
            'komentarz': 'Do it now!',
        }
        form = OrderForm(data=order_data)
        assert Order.objects.all().count() == 0
        assert 'Błędny numer telefonu' in form['numer_telefonu'].errors
        assert form.is_valid() == False


class TestImageForm():
    """Test case for ImageForm."""

    def test_image_form_object_created(self):
        """Test that image object is created through form."""

        image_data = {
            'tytuł': 'test1',
            'obraz_opis': 'Opis test',
        }
        form = ImageForm(data=image_data)
        assert form.is_valid()
        assert Image.objects.all().count() == 0
        form.is_valid()
        form.save()
        assert Image.objects.all().count() == 1
        assert Image.objects.filter(tytuł='test1').exists() == True


class TestGalleryForm():
    """Test case for GalleryForm."""

    def test_gallery_form_object_created(self, example_user):

        image = Image.objects.create(
            tytuł='Test image',
            obraz_opis='Test opis',
        )
        user = example_user
        gallery_data = {
            'tytuł': 'Test',
            'opis_modelu': 'Opis modelu',
            'zdjęcia': [image.id, ],
            'dodał': user.id,
        }
        form = GalleryForm(data=gallery_data)
        assert form.is_valid()
        assert Gallery.objects.all().count() == 0
        form.is_valid()
        form.save()
        assert Gallery.objects.all().count() == 1
        assert Gallery.objects.filter(tytuł='Test').exists() == True

    def test_gallery_form_clean_zdjęcia(self):
        pass
