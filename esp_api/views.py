from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json

from .models import SensorData



def index(request):
    return render(request, 'index.html') #returns the index.html template

@csrf_exempt
def receive_data(request):
    print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        temperature = data['temperature']
        humidity = data['humidity']
        #print(data)
        #temperature = request.POST.get('temperature')
        #humidity = request.POST.get('humidity')
        #print(f'{temperature}°C, {humidity}%')
        #temperature = request.GET.get('temperature')
        #humidity = request.GET.get('humidity')
        timestamp = timezone.now()
        SensorData.objects.create(temperature=temperature, humidity=humidity, timestamp=timestamp)
        return render(request, 'received.html')
    elif request.method == 'GET':
        records = SensorData.objects.all()

        # Format data for chart
        labels = [record.timestamp.strftime('%Y-%m-%d %H:%M:%S') for record in records]
        temperatureData = [record.temperature for record in records]
        humidityData = [record.humidity for record in records]

        # Pass data to template context
        context = {
            'labels': labels,
            'temperatureData': temperatureData,
            'humidityData': humidityData,
        }
        return render(request, 'chart.html', context)
    else:
        return HttpResponse("Invalid request method.")

