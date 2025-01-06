from django.db import models as dj
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.utils.timezone import now

from .models import PaymentCard, BankAccount, WeeklySchedule
from .data import UnitedStates
from .functions import get_document_upload_path

class USAddress(dj.Model):
    class Meta:
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'

    user = dj.ForeignKey(
        'users.CustomUser',
        on_delete=dj.CASCADE
    )
    name = dj.CharField(max_length=100)
    line_1 = dj.CharField(max_length=150)
    line_2 = dj.CharField(blank=True, max_length=150)
    city = dj.CharField(max_length=100)
    state = dj.CharField(
        max_length=50,
        choices=UnitedStates.states
    )
    zip_code = dj.CharField(
        max_length=5,
        validators=[
            MinLengthValidator(5)
        ]
    )
    
    def full_address(self):
        if self.line_2:
            return f'{self.line_1}, {self.line_2}, {self.city}, {self.state} {self.zip_code}'
        else:
            return f'{self.line_1}, {self.city}, {self.state} {self.zip_code}'

    def __str__(self):
        return f'{self.full_address()}'

class UserPaymentCard(PaymentCard):
    class Meta:
        verbose_name = 'User Payment Card'
        verbose_name_plural = 'User Payment Cards'

    user = dj.ForeignKey(
        'users.CustomUser',
        on_delete=dj.CASCADE
    )
    name = dj.CharField(max_length=25)
    primary = dj.BooleanField(default=True)

    def __str__(self):
        from .functions import format_name
        name = format_name(self.user, 'last, first MI')
        return f"{name} - {self.name}"
 

class Position(dj.Model):
    name = dj.CharField(max_length=50)
    description = dj.TextField(blank=True)

    def __str__(self):
        return self.name
    
class PayRate(dj.Model):
    class Meta:
        verbose_name = 'Staff Pay Rate'
        verbose_name_plural = 'Staff Pay Rates'
    
    frequency = dj.CharField(
        max_length=25,
        choices=[
            ('per year', 'per year'),
            ('per month', 'per month'),
            ('per hour', 'per hour'),
            ('variable', 'variable'),
        ]
    )
    amount = dj.DecimalField(
        max_digits=12, 
        decimal_places=2
    )


    def __str__(self):
        if self.frequency == 'variable':
            return self.frequency
        else:
            from .functions import format_currency
            amount = format_currency(self.amount)
            return f'{amount} {self.frequency}'
        
class UserDocument(dj.Model):
    name = dj.CharField(max_length=100)
    user = dj.ForeignKey(
        'users.CustomUser',
        on_delete=dj.CASCADE
    )
    file_date = dj.DateField(
        default=now
    )
    file = dj.FileField(upload_to=get_document_upload_path)
    
    def __str__(self):
        from .functions import format_name
        full_name = format_name(self.user, 'last, first MI')
        return f'{full_name} - {self.name}'
    
class EmploymentEvent(dj.Model):
    who = dj.ForeignKey(
        'users.CustomUser',
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='user_reported'
    )
    what = dj.CharField(max_length=50)
    when = dj.DateTimeField()
    why = dj.TextField()
    submitted_by = dj.ForeignKey(
        'users.CustomUser',
        blank=True,
        null=True,
        on_delete=dj.SET_NULL,
        related_name='reporting_user'
    )

    def __str__(self):
        from .functions import format_name
        name = format_name(self.who, format='last, first MI')
        return f'{name} {self.what} - {self.when.date()}'
    
class ScheduledTime(dj.Model):
    date = dj.DateField()
    start = dj.TimeField()
    end = dj.TimeField()

    def __str__(self):
        from .functions import format_date, format_time

        date = format_date(self.date, format='MMM-DD')
        start = format_time(self.start, format='HH:MM')
        end = format_time(self.end, format='HH:MM')

        return f'{date}: {start}-{end}'
    
class DepositAccount(BankAccount):
    class Meta:
        verbose_name = 'Deposit Account'
        verbose_name_plural = 'Deposit Accounts'
    
    user = dj.ForeignKey(
        'users.CustomUser',
        on_delete=dj.CASCADE
    )
    percentage = dj.PositiveIntegerField(
        validators=[
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        from .functions import format_name
        name = format_name(self.user, 'last, first MI')
        return f'{name} - {self.name} - {self.percentage}%'
    
class StaffAvailability(WeeklySchedule):
    class Meta:
        verbose_name = 'Staff Availability'
        verbose_name_plural = 'Staff Availabilities'
    
    user = dj.ForeignKey(
        'users.CustomUser',
        on_delete=dj.CASCADE
    )

    def __str__(self):
        from .functions import format_name
        name = format_name(self.user, 'last, first MI')
        return f"{name}"