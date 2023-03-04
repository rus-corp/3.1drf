from django.db import models
from django.utils import timezone

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField()
    date_time = models.DateTimeField(default=timezone.now)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE,
                                    related_name='measurements')
    

    def __str__(self) -> str:
        return f'{self.sensor_id} - {self.temperature}'
    

