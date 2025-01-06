from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models as dj
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField

from .managers import CustomUserManager
from .utils.fields import USAddress, UserPaymentCard, Position, PayRate, UserDocument, EmploymentEvent, ScheduledTime, DepositAccount, StaffAvailability
from .utils import get_profile_picture_upload_path

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = dj.EmailField(
        _('email'),
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
    
class Profile(dj.Model):
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    user = dj.OneToOneField(
        CustomUser, 
        on_delete=dj.CASCADE,
        related_name='user_profile'
    )

    first_name = dj.CharField(max_length=250)
    middle_name = dj.CharField(blank=True, max_length=250)
    last_name = dj.CharField(max_length=250)
    
    picture = dj.ImageField(
        blank=True,
        upload_to=get_profile_picture_upload_path
    )

    
    def __str__(self):
        return self.user.email
    
class ContactInfo(dj.Model):
    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'

    user = dj.OneToOneField(
        CustomUser, 
        on_delete=dj.CASCADE,
        related_name='user_contact'
    )
    phone_number = PhoneField(blank=True)
    phone_type = dj.CharField(
        max_length=25, 
        choices=[
            ('cell', 'cell'),
            ('landline', 'landline'),
        ],
        default='cell'
    )
    physical_address = dj.ForeignKey(
        USAddress,
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='user_physical_address'
    )
    mailing_address = dj.ForeignKey(
        USAddress,
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='user_mailing_address'
    )


    def __str__(self):
        return self.user.email

class CustomerProfile(dj.Model):
    class Meta:
        verbose_name = 'Customer Profile'
        verbose_name_plural = 'Customer Profiles'

    user = dj.OneToOneField(
        CustomUser, 
        on_delete=dj.CASCADE,
        related_name='user_customer_profile'
    )
    payment_methods = dj.ManyToManyField(
        UserPaymentCard,
        related_name='user_payment_cards'
    )
    transaction_history = dj.CharField(blank=True, max_length=25)

    def __str__(self):
        return self.user.email

class StaffProfile(dj.Model):
    class Meta:
        verbose_name = 'Staff Profile'
        verbose_name_plural = 'Staff Profiles'
    
    user = dj.OneToOneField(
        CustomUser, 
        on_delete=dj.CASCADE,
        related_name='user_staff_profile'
    )
    position = dj.ForeignKey(
        Position,
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='staff_position'
    )
    date_hired = dj.DateField(blank=True, null=True)
    date_left = dj.DateField(blank=True, null=True)
    reason_for_leaving = dj.CharField(blank=True, max_length=50)
    pay_rate = dj.ForeignKey(
        PayRate,
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='user_pay_rate'
    )
    documents = dj.ManyToManyField(
        UserDocument,
        blank=True,
        related_name='user_documents'
    )
    employment_events = dj.ManyToManyField(
        EmploymentEvent,
        blank=True,
        related_name='user_employment_events'
    )
    schedule = dj.ManyToManyField(
        ScheduledTime,
        blank=True,
        related_name='user_scheduled_times'
    )
    deposit_accounts = dj.ManyToManyField(
        DepositAccount,
        blank=True,
        related_name='staff_deposit_accounts'
    )
    availability_1 = dj.ForeignKey(
        StaffAvailability,
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='staff_availability_1'
    )
    availability_2 = dj.ForeignKey(
        StaffAvailability,
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='staff_availability_2'
    )

    def __str__(self):
        return self.user.email
