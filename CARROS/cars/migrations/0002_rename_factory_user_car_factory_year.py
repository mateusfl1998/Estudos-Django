# Generated by Django 5.0.1 on 2024-01-30 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='factory_user',
            new_name='factory_year',
        ),
    ]