# Generated by Django 5.1.4 on 2025-01-06 03:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_weeklyschedule_remove_bankaccount_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAvailability',
            fields=[
                ('weeklyschedule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.weeklyschedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff Availability',
                'verbose_name_plural': 'Staff Availabilities',
            },
            bases=('users.weeklyschedule',),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='availability_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_availability_1', to='users.staffavailability'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='availability_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_availability_2', to='users.staffavailability'),
        ),
    ]
