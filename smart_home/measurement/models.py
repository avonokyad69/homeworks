from django.db import models
from django import forms

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)
