from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, models.IntegerField, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
