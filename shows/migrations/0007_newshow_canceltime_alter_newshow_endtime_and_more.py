# Generated by Django 4.1.4 on 2023-02-18 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0006_alter_newshow_endtime_alter_newshow_starttime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newshow',
            name='cancelTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 7, 58, 12, 501106)),
        ),
        migrations.AlterField(
            model_name='newshow',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 7, 58, 12, 501106)),
        ),
        migrations.AlterField(
            model_name='newshow',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 7, 58, 12, 501106)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 7, 58, 12, 502162)),
        ),
    ]