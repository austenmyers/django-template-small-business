# Generated by Django 5.1.4 on 2025-01-06 00:51

import phone_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_contactinfo_phone_numbers_delete_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='phone_type',
            field=models.CharField(choices=[('cell', 'cell'), ('landline', 'landline')], default='cell', max_length=25),
        ),
    ]
