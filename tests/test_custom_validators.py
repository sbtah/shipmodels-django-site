import pytest
from django.core.exceptions import ValidationError
from users.models import fullname_validator
from orders.models import phone_number_validator


def test_fullname_validator():
    """Test that custom fullname_validator raises a proper errors."""

    with pytest.raises(ValidationError) as error:
        fullname_validator('a')

    with pytest.raises(ValidationError) as error:
        fullname_validator('12312')


def test_phone_number_validator():
    """Test that custom phone_number_validator raises an error."""

    with pytest.raises(ValidationError) as error:
        phone_number_validator(-11234)
