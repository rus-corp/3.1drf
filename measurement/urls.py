from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SensorViewSet, SensorDetailView, MeasurementCreateView



urlpatterns = [
    path('sensors/', SensorViewSet.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view())
]


