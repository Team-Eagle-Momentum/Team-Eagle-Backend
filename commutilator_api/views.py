# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Result
from .serializers import CalculatorSerializer, ResultSerializer


@api_view(['GET'])
def welcome(request):
    return Response({
        'team': 'Team Eagle',
        'description': 'Welcome to our app 👋'
    })


# allows POST of data to calculate
class Calculator(CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = CalculatorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # when a Result object is saved,
        # the user is set as the user that made the request


# allows GET of weekly result
class WeeklyResult(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    # def perform_create(self, serializer):
    #     serializer.save(weekly=(1/result.vehicle.mpg)*float(commute.distance)*float(commute.avg_gas_commute)*float(commute.days_per_week_commuting))
    
    # formula for calculating weekly result
    # inverse of MPG * distance * price * days/week
    # MPG = vehicle.mpg
    # distance = commute.distance
    # price = commute.avg_gas_commute
    # days = commute.days_per_week_commuting
    # (1/vehicle.mpg)*float(commute.distance)*float(commute.avg_gas_commute)*float(commute.days_per_week_commuting)
