# Generated by Django 4.0 on 2022-08-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commutilator_api', '0010_remove_vehicle_not_both_null_alter_vehicle_mpg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
