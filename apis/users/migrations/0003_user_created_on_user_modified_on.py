# Generated by Django 5.1.3 on 2025-02-15 06:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_user_avatar_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
