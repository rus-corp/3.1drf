from rest_framework import serializers

from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date_time', 'sensor_id']






class SensorDetailSerializer(serializers.ModelSerializer):
    measurement = MeasureSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']


