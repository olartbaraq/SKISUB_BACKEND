# Generated by Django 4.2.5 on 2023-09-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0002_alter_booking_adults_alter_booking_children_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='trip_type',
            field=models.CharField(choices=[('one_way', 'One Way'), ('round_trip', 'Round Trip')], default='one_way', max_length=20),
        ),
    ]
