import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from orders.models import Order
from gallery.models import Image, Gallery
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db


PANEL_URL = reverse('panel:panel')
LOGIN_URL = reverse('panel:login')
LOGOUT_URL = reverse('panel:logout')
CREATE_IMAGE_URL = reverse('panel:image-create')
LIST_ORDER_URL = reverse('panel:order-list')
LIST_IMAGEPOST_URL = reverse('gallery:image-list')
CREATE_ORDER_URL = reverse('orders:order-create')


@pytest.mark.parametrize('param', [
    ('about'),
    ('home'),
    ('cookies'),
    ('privacy-policy'),
    ('panel:login'),
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
        assert 'Wprowad?? poprawne warto??ci p??l email oraz has??o. Uwaga: wielko???? liter ma znaczenie.' in html


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


# Order related Test cases.
class TestOrderCreateView():
    """Test cases for Order's Public CreateView."""

    def test_create_order_view_saves_data(self, client, order_data):
        """Test that order can be created in database via View."""

        assert Order.objects.all().count() == 0
        response = client.post(CREATE_ORDER_URL, data=order_data)
        assert Order.objects.all().count() == 1
        assert Order.objects.filter(email='test@test.com').exists() == True
        assert response.status_code == 302


class TestOrderUpdateView():
    """Test cases for OrderUpdateView."""

    def test_update_order_view_without_user(self, client):
        """Test that order can not be updated without user logged in."""

        data = {
            'imi??_i_nazwisko': 'Test tester',
            'numer_telefonu': 671671671,
            'email': 'test@test.com',
            'model': 'Ship',
            'komentarz': 'Do it asap!',
        }
        order = mixer.blend(Order, imi??_i_nazwisko='Joe Doe')
        assert Order.objects.all().count() == 1
        response = client.post(
            reverse('panel:order-update', kwargs={'pk': order.id}), data=data)
        assert response.status_code == 302
        assert Order.objects.filter(
            imi??_i_nazwisko='Test tester').exists() == False

    def test_update_order_view_user_logged_in(self, client, example_user):
        """Test that order can be updated with authenticated user."""

        user = example_user
        client.force_login(user)
        data = {
            'imi??_i_nazwisko': 'Test tester',
            'numer_telefonu': 671671671,
            'email': 'test@test.com',
            'model': 'Ship',
            'komentarz': 'Do it asap!',
        }
        order = mixer.blend(Order, imi??_i_nazwisko='Joe Doe')
        assert Order.objects.all().count() == 1
        response = client.post(
            reverse('panel:order-update', kwargs={'pk': order.id}), data=data)
        assert response.status_code == 302
        assert Order.objects.filter(
            imi??_i_nazwisko='Test tester').exists() == True


class TestOrderDeleteView():
    """Test cases for OrderUpdateView."""

    def test_delete_order_view_without_user(self, client):
        """Test that order can not be deleted without user logged in."""

        order = mixer.blend(Order, imi??_i_nazwisko='Joe Doe')
        assert Order.objects.all().count() == 1
        response = client.post(
            reverse('panel:order-delete', kwargs={'pk': order.id}))
        assert response.status_code == 302
        assert Order.objects.all().count() == 1
        assert Order.objects.filter(
            imi??_i_nazwisko='Joe Doe').exists() == True

    def test_delete_order_view_user_logged_in(self, client, example_user):
        """Test that order can be deleted by authenticated user."""

        user = example_user
        client.force_login(user)
        order = mixer.blend(Order, imi??_i_nazwisko='Joe Doe')
        assert Order.objects.all().count() == 1
        response = client.post(
            reverse('panel:order-delete', kwargs={'pk': order.id}))
        assert response.status_code == 302
        assert Order.objects.all().count() == 0
        assert Order.objects.filter(
            imi??_i_nazwisko='Joe Doe').exists() == False


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


# Image related Test cases.
class TestImagePostListView():
    """Test cases for public ImagePostListView."""

    def test_list_image_view_lists_data(self, client):
        """Test that image list view properly lists data."""

        image_1 = mixer.blend(Image)
        image_2 = mixer.blend(Image)
        response = client.get(LIST_IMAGEPOST_URL)
        assert Image.objects.all().count() == 2
        assert len(response.context_data['object_list']) == 2
        assert response.status_code == 200


class TestImagePostDetailView():
    """Test cases for public ImagePostDetailView."""

    def test_detail_image_view_return_data(self, client):
        """Test that image detail view properly returns data."""

        image_1 = mixer.blend(Image, tytu??='test slug')
        response = client.get(reverse(
            'gallery:image-detail',
            args=[image_1.slug]),
        )
        html = response.content.decode('utf8')
        assert '<title>Shipmodels | test slug</title>' in html
        assert response.status_code == 200


class TestImagePostCreateView():
    """Test cases for ImagePostCreateView - this view is for logged users only."""

    def test_image_post_create_view_without_user(self, client):
        """Test that image cant be created by unauthenticated user."""

        assert Image.objects.all().count() == 0
        response = client.get(CREATE_IMAGE_URL)
        assert response.status_code == 302

    def test_image_post_create_view_user_logged_in(self, client, example_user):
        """Test that image is created by authenticated user."""

        user = example_user
        image_data = {
            'tytu??': 'test',
            'obraz_opis': 'opis',
            'doda??': user.id
        }
        client.force_login(user)
        assert Image.objects.all().count() == 0
        response = client.post(CREATE_IMAGE_URL, data=image_data, follow=True)
        html = response.content.decode('utf8')
        assert '<title>Shipmodels | Admin</title>' in html
        assert Image.objects.all().count() == 1
        assert response.status_code == 200


class TestImagePostUpdateView():
    """Test cases for ImagePostUpdateView - this view is for logged users only."""

    def test_image_post_update_view_without_user(self, client):
        """Test that image can not be updated without authenticated user."""

        data = {
            'tytu??': 'fail',
            'obraz_opis': 'test',
        }
        image = mixer.blend(Image, tytu??='test')
        assert Image.objects.all().count() == 1
        response = client.post(
            reverse('panel:image-update', args=[image.id]), data=data)
        assert response.status_code == 302
        image.refresh_from_db()
        assert Image.objects.filter(tytu??='fail').exists() == False

    def test_image_post_update_view_user_logged_in(self, client, example_user):
        """Test that image post can be updated"""

        user = example_user
        client.force_login(user)
        data = {
            'tytu??': 'fail',
            'obraz_opis': 'test',
            'doda??': user.id
        }
        image = mixer.blend(Image, tytu??='test')
        assert Image.objects.all().count() == 1
        response = client.post(
            reverse('panel:image-update', args=[image.id]),
            data=data,
            follow=True
        )
        assert response.status_code == 200
        image.refresh_from_db()
        assert Image.objects.filter(tytu??='fail').exists() == True


class TestImagePostDeleteView():
    """Test cases for ImagePostDeleteView - this view is for logged users only."""

    def test_image_post_delete_view_without_user(self, client):
        """Test that image can not be deleted by unauthenticated user."""

        assert Image.objects.all().count() == 0
        image = mixer.blend(Image, tytu??='test')
        assert Image.objects.all().count() == 1
        response = client.post(
            reverse('panel:image-delete', args=[image.id]),
        )
        assert response.status_code == 302
        assert Image.objects.all().count() == 1
        assert Image.objects.filter(tytu??='test').exists() == True

    def test_image_post_delete_view_user_logged_in(self, client, example_user):
        """Test that image post can be deleted"""

        user = example_user
        client.force_login(user)
        image = mixer.blend(Image, tytu??='test')
        assert Image.objects.all().count() == 1
        response = client.post(
            reverse('panel:image-delete', args=[image.id]),
        )
        assert response.status_code == 302
        assert Image.objects.all().count() == 0
        assert Image.objects.filter(tytu??='test').exists() == False


class Test_main_panel_view():
    """Test cases for main_panel_view."""

    def test_main_panel_view_without_user(self, client):
        """Test that only logged users can access mini admin panel."""

        response = client.get(PANEL_URL, follow=True)
        html = response.content.decode('utf8')
        assert '<title>Shipmodels | Login</title>' in html
        assert response.status_code == 200

    def test_main_panel_view_lists_data(self, client, example_user):
        """Test main_panel_view with logged user."""

        user = example_user
        client.force_login(user)
        order = mixer.blend(Order, full_name='tester tester')
        gallery = mixer.blend(Gallery, title='Test Ship')
        response = client.get(PANEL_URL)
        assert response.status_code == 200
        assert response.context['galleries_count'] == 1
        assert response.context['orders_count'] == 1
