# Generated by Django 2.2.2 on 2019-06-09 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20190609_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='height',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='width',
        ),
    ]
