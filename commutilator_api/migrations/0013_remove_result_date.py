# Generated by Django 4.0 on 2022-08-19 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commutilator_api', '0012_remove_calculationdata_unique_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='date',
        ),
    ]
