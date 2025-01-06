from django.db import models as dj
from django.core.validators import MinLengthValidator
from .data import PaymentCards


class PaymentCard(dj.Model):
    card_type = dj.CharField(
        max_length=25,
        choices=PaymentCards.card_types
    )
    card_brand = dj.CharField(
        max_length=25,
        choices=PaymentCards.brands
    )
    card_number = dj.CharField(
        max_length=19,
        validators=[
            MinLengthValidator(8)
        ]
    )
    expiration_date = dj.DateField()
    security_code = dj.CharField(
        max_length=4,
        validators=[
            MinLengthValidator(3)
        ]
    )
    billing_zip_code = dj.CharField(
        max_length=5,
        validators=[
            MinLengthValidator(5)
        ]
    )

class BankAccount(dj.Model):
    name = dj.CharField(max_length=50)
    routing_number = dj.CharField(
        max_length=9,
        validators=[
            MinLengthValidator(9)
        ]
    )
    account_number = dj.CharField(max_length=20,)
    
class WeeklySchedule(dj.Model):
    monday = dj.BooleanField(default=True)
    monday_from = dj.TimeField()
    monday_to = dj.TimeField()
    tuesday = dj.BooleanField(default=True)
    tuesday_from = dj.TimeField()
    tuesday_to = dj.TimeField()
    wednesday = dj.BooleanField(default=True)
    wednesday_from = dj.TimeField()
    wednesday_to = dj.TimeField()
    thursday = dj.BooleanField(default=True)
    thursday_from = dj.TimeField()
    thursday_to = dj.TimeField()
    friday = dj.BooleanField(default=True)
    friday_from = dj.TimeField()
    friday_to = dj.TimeField()
    saturday = dj.BooleanField(default=True)
    saturday_from = dj.TimeField()
    saturday_to = dj.TimeField()
    sunday = dj.BooleanField(default=True)
    sunday_from = dj.TimeField()
    sunday_to = dj.TimeField()

