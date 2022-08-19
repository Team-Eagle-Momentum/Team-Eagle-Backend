# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

from datetime import date, datetime
import calendar

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from commutilator_api.models import CalculationData, Commute, Result, Vehicle
from commutilator_api.serializers import PostCalculationDataSerializer, VehicleSerializer, CommuteSerializer, ResultDetailSerializer


@api_view(['GET'])
def welcome(request):
    return Response({
        'team': 'Team Eagle',
        'message': 'Welcome to our app 👋'
    })


# allows POST of vehicle data
class CreateVehicle(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# allows POST of commute data
class CreateCommute(CreateAPIView):
    queryset = Commute.objects.all()
    serializer_class = CommuteSerializer 


# allows POST of calcuation data
class CreateCalculationData(CreateAPIView):
    queryset = CalculationData.objects.all()
    serializer_class = PostCalculationDataSerializer

    def perform_create(self, serializer):
        commute = Commute.objects.get(pk=self.request.data['commute'])
        vehicle = Vehicle.objects.get(pk=self.request.data['vehicle'])
        today = date.today()

        daily_result = round((((commute.distance * 2) / vehicle.mpg) * commute.avg_gas_commute), 2)

        weekly_result = round((((commute.distance * 2) / vehicle.mpg) * commute.avg_gas_commute) * commute.days_per_week_commuting, 2)

        monthly_result = round((((commute.distance * 2) / vehicle.mpg) * commute.avg_gas_commute) * (commute.days_per_week_commuting * (len(calendar.monthcalendar(today.year, today.month)))), 2)

        annual_result = round((((commute.distance * 2) / vehicle.mpg) * commute.avg_gas_commute) * commute.days_per_week_commuting * 52, 2)

        date_result_title = datetime.now()
        result_object = Result.objects.create(daily=daily_result,
                                              weekly=weekly_result,
                                              monthly=monthly_result,
                                              title=date_result_title,
                                              annual=annual_result)

        serializer.save(commute=commute, vehicle=vehicle, result=result_object)


# allows GET of all result data
class ResultDetail(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultDetailSerializer


# allows GET of all calculation data
# class AllCalcDetail(RetrieveAPIView):
#     queryset = CalculationData.objects.all()
#     serializer_class = GetCalculationDataSerializer
#     permission_classes = [IsAuthenticated]
