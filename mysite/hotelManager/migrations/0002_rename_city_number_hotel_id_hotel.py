# Generated by Django 4.0 on 2021-12-08 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='city_number',
            new_name='id_hotel',
        ),
    ]
