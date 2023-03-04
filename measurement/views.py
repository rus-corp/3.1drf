# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasureSerializer






class SensorViewSet(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        sen = Sensor.objects.create(
            name = request.data['name'],
            description = request.data['description']
        )
        return Response({'sensors': SensorSerializer(sen).data})
    
class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasureSerializer

    def post(self, request):
        mes = Measurement.objects.create(
            sensor_id_id = request.data['sensor'],
            temperature = request.data['temperature']
        )
        return Response({'sensors': MeasureSerializer(mes).data})

    


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



    


    
