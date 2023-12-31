# Generated by Django 4.2.5 on 2023-10-01 22:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbooking', '0002_car_end_date_car_start_date_alter_booking_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='price_per_hour',
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='car',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='car',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
