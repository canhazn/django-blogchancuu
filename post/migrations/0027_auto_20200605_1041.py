# Generated by Django 3.0.6 on 2020-06-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_auto_20200604_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]