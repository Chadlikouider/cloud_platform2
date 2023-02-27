from django.db import models


class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField('date published')

    def _str_(self):
        return f'{self.temperature}°C, {self.humidity}% ({self.timestamp})'