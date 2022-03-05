import pytest
from orders.models import Order
from orders.forms import OrderForm


pytestmark = pytest.mark.django_db


class TestOrderForm():
    """Test case for OrderForm."""

    def test_form_object_created(self, client):
        """Test that object is created through form."""

        order_data = {
            'imię_i_nazwisko': 'Test Tester',
            'numer_telefonu': 712712712,
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
