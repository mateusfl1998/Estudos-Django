# Generated by Django 5.0.1 on 2024-02-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(default=2, upload_to='cars/'),
            preserve_default=False,
        ),
    ]