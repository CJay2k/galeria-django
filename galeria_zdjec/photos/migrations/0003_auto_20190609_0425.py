# Generated by Django 2.2.2 on 2019-06-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20190609_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
