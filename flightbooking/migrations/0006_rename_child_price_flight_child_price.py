# Generated by Django 4.2.5 on 2023-09-30 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0005_alter_flight_child_price_alter_flight_adult_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='Child_price',
            new_name='child_price',
        ),
    ]
