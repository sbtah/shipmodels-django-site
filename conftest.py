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
        'full_name': 'Test tester',
        'phone_number': '123123123',
        'email': 'test@test.com',
        'model': 'Statek',
        'comment': 'This is a test',
        'created': '2022-04-01',
        'updated': '2022-04-01',
    }


@pytest.fixture
def example_user():
    return get_user_model().objects.create_user(
        email='test@test.com',
        full_name='tester',
        password='testpass123!'
    )
