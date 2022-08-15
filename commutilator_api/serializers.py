from rest_framework import serializers
from .models import Vehicle, Commute, Result


# used in Calculator view
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
