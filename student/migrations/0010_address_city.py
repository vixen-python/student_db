# Generated by Django 3.0.10 on 2021-07-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_mediadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='Praha', max_length=64),
            preserve_default=False,
        ),
    ]
