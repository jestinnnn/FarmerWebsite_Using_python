# Generated by Django 4.2.8 on 2023-12-13 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0011_remove_loan_category_remove_loan_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.TextField(max_length=5, null=True)),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmerapp.farmer')),
            ],
        ),
    ]