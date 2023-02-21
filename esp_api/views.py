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
    print(request.body.decode('utf-8'))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        temperature = data['temperature']
        humidity = data['humidity']
        #temperature = request.GET.get('temperature')
        #humidity = request.GET.get('humidity')
        timestamp = timezone.now()
        SensorData.objects.create(temperature=temperature, humidity=humidity, timestamp=timestamp)
        return HttpResponse("Data received successfully.")
    else:
        return HttpResponse("Invalid request method.")

