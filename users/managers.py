from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique
    identifier for authentication instead of username.
    """
    def create_user(self, email, password, **extra_fields):
        # Create and save a user with the given email and password
        if not email:
            raise ValueError(_('Email is required.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        # Create a user with Super User status
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser requires is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser requires is_superuser=True'))
        return self.create_user(email, password, **extra_fields)