from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vehicle(TimeStamp):
    make = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    mpg = models.IntegerField()


class Commute(TimeStamp):
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    distance = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True)
    days_per_week_commuting = models.IntegerField()
    start_avg_gas = models.DecimalField(max_digits=3, decimal_places=2,
                                        null=True)
    end_avg_gas = models.DecimalField(max_digits=3, decimal_places=2,
                                      null=True)
    avg_gas_commute = models.DecimalField(max_digits=3, decimal_places=2,
                                          null=True)


class Result(TimeStamp):
    daily = models.DecimalField(max_digits=10, decimal_places=2,
                                null=True)
    weekly = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True)
    monthly = models.DecimalField(max_digits=10, decimal_places=2,
                                  null=True)
    annual = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True)
    title = models.CharField(max_length=255,
                             null=True)


class CalculationData(TimeStamp):
    user = models.ForeignKey('auth.user', related_name='calculations',
                             on_delete=models.CASCADE, null=True)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    commute = models.OneToOneField(Commute, on_delete=models.CASCADE)
    result = models.OneToOneField(Result, on_delete=models.CASCADE, null=True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['vehicle', 'commute', 'result'],
    #                                 name='unique_result')
    #     ]
