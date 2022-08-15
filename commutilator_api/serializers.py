from rest_framework import serializers
from .models import Vehicle, Commute, Result


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = [
            'make',
            'model',
            'year',
            'mpg',
        ]


class CommuteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commute
        fields = [
            'start_location',
            'end_location',
            'distance',
            'days_per_week_commuting',
            'start_avg_gas',
            'end_avg_gas',
            'avg_gas_commute',
        ]


class CalculatorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Result
        fields = [
            'id',
            'user',
            'vehicle',
            'commute',
        ]


# used in WeeklyResult view
class ResultSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Result
        fields = [
            'id',
            'user',
            'daily',
            'weekly',
            'monthly',
            'annual',
        ]
