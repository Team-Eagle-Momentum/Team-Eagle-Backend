# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Vehicle, Commute, Result
from .serializers import VehicleSerializer, CommuteSerializer, ResultSerializer


@api_view(['GET'])
def welcome(request):
    return Response({
        'team': 'Team Eagle',
        'description': 'Welcome to our app 👋'
    })


# allows POST of vehicle data
class CreateVehicle(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# allows POST of commute data
class CreateCommute(CreateAPIView):
    queryset = Commute.objects.all()
    serializer_class = CommuteSerializer


# allows GET of result data
class ResultDetail(RetrieveAPIView):
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
