from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_number_validator(val):
    """Custom validator for orders's phone_number"""

    if not all(x.isnumeric() for x in val):
        raise ValidationError(
            _('Błędny numer telefonu'),
            params={'value': val}
        )

    elif val == '':
        raise ValidationError(
            _('Błędny numer telefonu'),
            params={'value': val}
        )


def fullname_validator(val):
    """Custom validator for user's full_name"""

    if len(val) < 2:
        raise ValidationError(
            _('Błędne Imię i Nazwisko'),
            params={'value': val}
        )

    elif not all(x.isalpha() or x.isspace() for x in val):
        raise ValidationError(
            _('Błędne Imię i Nazwisko'),
            params={'value': val}
        )
