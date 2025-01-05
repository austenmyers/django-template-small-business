from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models as dj
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomerUser(AbstractBaseUser, PermissionsMixin):
    email = dj.EmailField(
        _('email_address'),
        unique=True
    )
    is_staff = dj.BooleanField(default=False)
    is_active = dj.BooleanField(default=True)
    date_joined = dj.DateTimeField(
        default=timezone.now
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email