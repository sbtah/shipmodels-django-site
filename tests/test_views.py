import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model


pytestmark = pytest.mark.django_db
LOGIN_URL = reverse('panel:login')
LOGOUT_URL = reverse('panel:logout')


@pytest.mark.parametrize('param', [

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
        assert response.status_code == 200
        html = response.content.decode('utf8')
        assert 'Bye!' in html
