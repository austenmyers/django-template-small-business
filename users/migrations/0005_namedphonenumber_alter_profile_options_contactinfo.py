# Generated by Django 5.1.4 on 2025-01-06 00:44

import django.db.models.deletion
import phone_field.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamedPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_type', models.CharField(choices=[('cellular', 'cellular'), ('landline', 'landline')], max_length=25)),
                ('number', phone_field.models.PhoneField(max_length=31)),
            ],
            options={
                'verbose_name': 'Phone Number',
                'verbose_name_plural': 'Phone Numbers',
            },
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_contact', to=settings.AUTH_USER_MODEL)),
                ('phone_numbers', models.ManyToManyField(related_name='user_phone_numbers', to='users.namedphonenumber')),
            ],
            options={
                'verbose_name': 'Contact Information',
                'verbose_name_plural': 'Contact Information',
            },
        ),
    ]
