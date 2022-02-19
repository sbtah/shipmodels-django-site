from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """Custom User Manager Class"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves new user."""

        if not email:
            raise ValueError(_('Users must have an email address'))
        elif get_user_model().objects.filter(email=email).exists():
            raise ValueError(_('You cant not use this email address'))
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves new user."""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user class with usernamefield being an email."""

    email = models.EmailField(
        unique=True,
        max_length=100,
        help_text=(_('Your email address')),
    )
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
