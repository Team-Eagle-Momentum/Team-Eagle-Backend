from rest_framework import serializers
from .models import Vehicle, Commute, Result


# used in Calculator view
class CalculatorSerializer(serializers.ModelSerializer):
    # weekly = 

    class Meta:
        model = Result
        fields = [
            'user',
            'weekly',
            'vehicle',
            'commute',
        ]
