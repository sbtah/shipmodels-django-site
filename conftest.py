import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_data():
    return {
        'username': 'test@test.com',
        'password': 'testpass123!',
    }


@pytest.fixture
def order_data():
    return {
        'imię_i_nazwisko': 'Test tester',
        'numer_telefonu': '123123123',
        'email': 'test@test.com',
        'model': 'Statek',
        'komentarz': 'This is a test',
        'dodano': '2022-04-01',
        'zaktualizowano': '2022-04-01',
    }


@pytest.fixture
def example_user():
    return get_user_model().objects.create_user(
        email='test@test.com',
        full_name='tester',
        password='testpass123!'
    )
