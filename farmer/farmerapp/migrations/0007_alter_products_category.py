# Generated by Django 4.2.8 on 2023-12-12 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0006_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=-2010, on_delete=django.db.models.deletion.CASCADE, to='farmerapp.category'),
            preserve_default=False,
        ),
    ]
