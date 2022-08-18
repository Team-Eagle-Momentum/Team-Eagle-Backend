"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from commutilator_api import views as commutilator_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    path('', commutilator_views.welcome),
    path('vehicle/', commutilator_views.CreateVehicle.as_view(),
         name='vehicle'),
    path('commute/', commutilator_views.CreateCommute.as_view(),
         name='commute'),
    path('calc/', commutilator_views.CreateCalculationData.as_view(),
         name='calc'),
    path('result/<int:pk>', commutilator_views.WeeklyResult.as_view(),
         name='result'),
    path('detail/<int:pk>', commutilator_views.ResultDetail.as_view(),
         name='detail'),
]
