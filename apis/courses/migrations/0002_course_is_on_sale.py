# Generated by Django 5.1.4 on 2025-02-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_on_sale',
            field=models.BooleanField(default=False),
        ),
    ]
