# Generated by Django 4.0.5 on 2022-10-27 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 20, 0, 41, 403137)),
        ),
    ]
