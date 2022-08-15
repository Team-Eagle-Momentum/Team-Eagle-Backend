# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Result
from .serializers import CalculatorSerializer


@api_view(['GET'])
def welcome(request):
    return Response({
        'team': 'Team Eagle',
        'description': 'Welcome to our app 👋'
    })


# allows POST of data to return weekly result
class Calculator(CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = CalculatorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # when a Result object is saved,
        # the user is set as the user that made the request
