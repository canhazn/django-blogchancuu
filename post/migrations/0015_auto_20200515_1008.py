# Generated by Django 3.0.6 on 2020-05-15 03:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20200515_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 3, 8, 3, 833442, tzinfo=utc), editable=False),
        ),
    ]
