# Generated by Django 2.0 on 2018-01-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0004_spot_typeproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeproduct',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icon_image'),
        ),
    ]
