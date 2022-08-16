# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from commutilator_api.models import CalculationData, Commute, Result, Vehicle
from commutilator_api.serializers import CalculationDataSerializer, VehicleSerializer, CommuteSerializer


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

class CreateCalculationData(CreateAPIView):
    queryset = CalculationData.objects.all()
    serializer_class = CalculationDataSerializer 

    def perform_create(self, serializer):
        commute = Commute.objects.get(pk=self.request.data['commute'])
        vehicle = Vehicle.objects.get(pk=self.request.data['vehicle'])
        weekly_result = round(((commute.distance / vehicle.mpg) * commute.avg_gas_commute) * commute.days_per_week_commuting, 2)
        result_object = Result.objects.create(weekly=weekly_result)
        serializer.save(commute=commute, vehicle=vehicle, result=result_object)


# allows GET of result data
# class ResultDetail(RetrieveAPIView):
#     pass
    # queryset = Result.objects.all()
    # serializer_class = ResultSerializer

    # def perform_create(self, serializer):
    #     serializer.save(weekly=(1/result.vehicle.mpg)*float(commute.distance)*float(commute.avg_gas_commute)*float(commute.days_per_week_commuting))

    # formula for calculating weekly result
    # inverse of MPG * distance * price * days/week
    # MPG = vehicle.mpg
    # distance = commute.distance
    # price = commute.avg_gas_commute
    # days = commute.days_per_week_commuting
    # (1/vehicle.mpg)*float(commute.distance)*float(commute.avg_gas_commute)*float(commute.days_per_week_commuting)
