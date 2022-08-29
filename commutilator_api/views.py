from datetime import date, datetime
import calendar
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from commutilator_api.models import CalculationData, Commute, Result, Vehicle
from commutilator_api.serializers import CalculationDataSerializer, VehicleSerializer, CommuteSerializer, ResultDetailSerializer
from commutilator_api.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend


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

    def perform_create(self, serializer):
        start_avg = self.request.data['start_avg_gas']
        end_avg = self.request.data['end_avg_gas']
        if start_avg == 0 and end_avg != 0:
            avg_gas_commute = end_avg
        elif end_avg == 0 and start_avg != 0:
            avg_gas_commute = start_avg
        else:
            avg_gas_commute = ((start_avg + end_avg)/2)

        serializer.save(avg_gas_commute=avg_gas_commute)


# allows POST of calcuation data
class CreateCalculationData(CreateAPIView):
    queryset = CalculationData.objects.all()
    serializer_class = CalculationDataSerializer

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


class AllCalcDetailList(generics.ListAPIView):
    queryset = CalculationData.objects.order_by("-created_at")
    serializer_class = CalculationDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, IsOwnerFilterBackend]


# allows GET, PUT, PATCH, DELETE of calculation data
class AllCalcDetail(RetrieveUpdateDestroyAPIView):
    queryset = CalculationData.objects.all()
    serializer_class = CalculationDataSerializer
    # TODO: add permission class after testing auth flow on frontend


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_update(serializer)

    def retrieve(self, request, *args, **kwargs):
        owner_qs = self.queryset.filter(user=self.request.user)
        owner_object = owner_qs.get(pk=self.kwargs['pk'])
        serializer = self.get_serializer(owner_object)
        return Response(serializer.data)

