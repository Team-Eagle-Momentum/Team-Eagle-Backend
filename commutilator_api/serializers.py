from rest_framework import serializers
from commutilator_api.models import CalculationData, Vehicle, Commute, Result


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class CommuteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commute
        fields = '__all__'


class CalculationDataSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CalculationData 
        fields = '__all__'
        depth = 1


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = [
            'id',
            'daily',
            'weekly',
            'monthly',
            'annual',
        ]
