# Generated by Django 4.0 on 2022-08-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commutilator_api', '0011_alter_result_title'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='calculationdata',
            name='unique_result',
        ),
    ]