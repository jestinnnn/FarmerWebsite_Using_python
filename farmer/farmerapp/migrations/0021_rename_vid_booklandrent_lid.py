# Generated by Django 4.2.8 on 2023-12-20 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0020_bookvehiclerent_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booklandrent',
            old_name='vid',
            new_name='lid',
        ),
    ]
