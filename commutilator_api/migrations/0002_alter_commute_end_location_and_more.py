# Generated by Django 4.0 on 2022-08-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commutilator_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commute',
            name='end_location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='commute',
            name='start_location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='result',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
