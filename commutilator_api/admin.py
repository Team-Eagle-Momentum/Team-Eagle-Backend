from django.contrib import admin
from .models import Vehicle, Commute, Result, CalculationData

admin.site.register(Vehicle)
admin.site.register(Commute)
admin.site.register(Result)
admin.site.register(CalculationData)
