# Generated by Django 3.0.6 on 2020-06-10 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_auto_20200605_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
