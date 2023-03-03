# Generated by Django 4.1.4 on 2023-01-22 22:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_reservation_date_reservation_starttime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newshow',
            name='date',
        ),
        migrations.RemoveField(
            model_name='newshow',
            name='remainingSeats',
        ),
        migrations.AlterField(
            model_name='newshow',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 22, 58, 24, 16166)),
        ),
        migrations.AlterField(
            model_name='newshow',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 22, 58, 24, 16166)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='title',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shows.newshow'),
        ),
    ]
