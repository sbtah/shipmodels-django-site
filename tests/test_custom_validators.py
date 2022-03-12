import pytest
from django.core.exceptions import ValidationError
from core.validators import fullname_validator, phone_number_validator


def test_fullname_validator():
    """Test that custom fullname_validator raises a proper errors."""

    with pytest.raises(ValidationError) as error:
        fullname_validator('a')

    with pytest.raises(ValidationError) as error:
        fullname_validator('12312')


def test_phone_number_validator():
    """Test that custom phone_number_validator raises an error."""

    with pytest.raises(ValidationError) as error:
        phone_number_validator("TEST")

    with pytest.raises(ValidationError) as error:
        phone_number_validator("A")

    with pytest.raises(ValidationError) as error:
        phone_number_validator("123AVB")

    with pytest.raises(ValidationError) as error:
        phone_number_validator("    ")

    with pytest.raises(ValidationError) as error:
        phone_number_validator("")
