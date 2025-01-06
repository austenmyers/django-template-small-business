# Generated by Django 5.1.4 on 2025-01-06 01:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_usaddress_contactinfo_mailing_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_methods', models.CharField(blank=True, max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer Profile',
                'verbose_name_plural': 'Customer Profiles',
            },
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_hired', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_staff_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff Profile',
                'verbose_name_plural': 'Staff Profiles',
            },
        ),
    ]
