from sqlite3 import Timestamp
from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vehicle(Timestamp):
    make = models.IntegerField(null=True)
    model = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    mpg = models.IntegerField(null=True)


class Commute(Timestamp):
    start_location = models.TextField(max_length=400)
    end_location = models.TextField(max_length=400)
    distance = models.IntegerField()
    days_per_week_commuting = models.IntegerField()
    start_avg_gas = models.IntegerField(null=True)
    end_avg_gas = models.IntegerField(null=True)
    avg_gas_commute = models.IntegerField(null=True)


class Result(TimeStamp):
    user = models.ForeignKey('auth.user', related_name='user', on_delete=models.CASCADE)
    daily = models.IntegerField(null=True) 
    weekly = models.IntegerField(null=True) 
    monthly = models.IntegerField(null=True) 
    annual = models.IntegerField(null=True) 
    date = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=400)
    vehicle = models.OneToOneField('Vehicle', on_delete=models.CASCADE, null=True)
    commute = models.OneToOneField('Commute', on_delete=models.CASCADE, null=True)
