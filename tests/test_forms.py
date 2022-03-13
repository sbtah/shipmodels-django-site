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
