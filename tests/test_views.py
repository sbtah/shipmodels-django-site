import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from orders.models import Order
from gallery.models import ImagePost, ImageGallery
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db
LOGIN_URL = reverse('panel:login')
LOGOUT_URL = reverse('panel:logout')
CREATE_ORDER_URL = reverse('orders:order-create')
LIST_ORDER_URL = reverse('panel:order-list')
LIST_IMAGEPOST_URL = reverse('gallery:gallery-list')


@pytest.mark.parametrize('param', [
    ('about'),
    ('panel:login'),
    ('home'),
    ('orders:order-create'),
    ('gallery:gallery-list'),
    ('gallery:image-list'),
])
def test_response_from_public_urls(client, param):
    """Test reponse from public urls."""

    temp_url = reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


class TestLoginCustomUserView():
    """Test cases for LoginCustomUserView."""

    def test_user_login_succesful(self, client, user_data):
        """Test that user can log in at proper endpoint."""

        assert get_user_model().objects.all().count() == 0
        email = 'test@test.com'
        password = 'testpass123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        assert get_user_model().objects.all().count() == 1
        response = client.post(
            LOGIN_URL,
            data=user_data,
        )
        assert response.status_code == 302
        assert response.url == reverse('home')

    def test_user_login_fails(self, client, user_data):
        """Test login with bad data raises an error."""

        email = 'test2@test2.com'
        password = 'testpass123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        response = client.post(
            LOGIN_URL,
            data=user_data
        )
        # Decode response to HTML to check for error message.
        html = response.content.decode('utf8')
        assert response.status_code == 200
        assert 'Please enter a correct email and password. Note that both fields may be case-sensitive.' in html


class TestLogoutCustomUserView():
    """Test cases for LogoutCustomUserView."""

    def test_user_logout_without_user(self, client):
        """Test that view is not allowed for public use."""

        response = client.get(LOGOUT_URL)
        assert response.status_code == 302

    def test_user_logged_out(self, client):
        """Test that user cant be logged out."""

        email = 'test2@test2.com'
        password = 'testpass123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        client.force_login(user=user)
        response = client.get(LOGOUT_URL)
        assert response.status_code == 302


class TestOrderCreateView():
    """Test cases for Order's Public CreateView."""

    def test_create_order_view_saves_data(self, client, order_data):
        """Test that order can be created in database via View."""

        assert Order.objects.all().count() == 0
        response = client.post(CREATE_ORDER_URL, data=order_data)
        assert Order.objects.all().count() == 1
        assert Order.objects.filter(email='test@test.com').exists() == True
        assert response.status_code == 302
        assert response.url == reverse('home')


class TestOrderListView():
    """Test cases for Order's private ListView."""

    def test_list_order_view_without_user(self, client):
        """Test endpoint access of order list view without logged user."""

        response = client.get(LIST_ORDER_URL)
        assert response.status_code == 302

    def test_list_order_view_user_logged_in(self, client, example_user):
        """Test OrderListView with authenticated user."""

        user = example_user
        order_1 = mixer.blend(Order)
        order_2 = mixer.blend(Order)
        client.force_login(user)
        response = client.get(LIST_ORDER_URL)
        assert len(response.context['orders']) == 2
        assert response.status_code == 200


class TestOrderDetailView():
    """Test cases for OrderDetailView."""

    def test_detail_order_view_without_user(self, client):
        """Test endpoint access of order list view without logged user."""

        order = mixer.blend(Order)
        response = client.get(
            reverse('panel:order-detail', kwargs={'pk': order.id}))
        assert response.status_code == 302

    def test_detail_order_view_user_logged_in(self, client, example_user):
        """Test OrderDetailView with user logged in."""

        user = example_user
        client.force_login(user)
        order = mixer.blend(Order)
        response = client.get(
            reverse('panel:order-detail', kwargs={'pk': order.id}))
        assert response.context_data['object'] != ''
        assert response.status_code == 200


class TestImagePostListView():
    """Test cases for ImagePostListView."""

    def test_list_image_view_lists_data(self, client):
        """Test that image list properly lists data."""

        image_1 = mixer.blend(ImagePost)
        image_2 = mixer.blend(ImagePost)
        response = client.get(LIST_IMAGEPOST_URL)
        assert len(response.context_data['object_list']) == 2
        assert response.status_code == 200
