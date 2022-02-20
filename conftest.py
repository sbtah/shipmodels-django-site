import pytest


@pytest.fixture
def user_data():
    return {
        'username': 'test@test.com',
        'password': 'testpass123!',
    }
