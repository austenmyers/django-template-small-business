# Generated by Django 5.1.4 on 2025-01-06 02:21

import django.db.models.deletion
import django.utils.timezone
import users.utils.functions
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_payrate_staffprofile_pay_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_date', models.DateField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to=users.utils.functions.get_document_upload_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='documents',
            field=models.ManyToManyField(related_name='user_documents', to='users.userdocument'),
        ),
    ]