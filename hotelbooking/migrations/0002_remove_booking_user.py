# Generated by Django 4.2.5 on 2023-10-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
