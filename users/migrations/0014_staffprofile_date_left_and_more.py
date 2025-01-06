# Generated by Django 5.1.4 on 2025-01-06 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_customerprofile_transaction_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='date_left',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='reason_for_leaving',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]