# Generated by Django 2.2.2 on 2019-06-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20190609_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, height_field='height', null=True, upload_to='', width_field='width'),
        ),
    ]