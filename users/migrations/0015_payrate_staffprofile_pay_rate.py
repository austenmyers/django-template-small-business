# Generated by Django 5.1.4 on 2025-01-06 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_staffprofile_date_left_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(choices=[('per year', 'per year'), ('per month', 'per month'), ('per hour', 'per hour'), ('variable', 'variable')], max_length=25)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'verbose_name': 'Staff Pay Rate',
                'verbose_name_plural': 'Staff Pay Rates',
            },
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='pay_rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_pay_rate', to='users.payrate'),
        ),
    ]