from django.shortcuts import render
from . import forms
from . import models
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def normal_leg_filter(request):
    if(request.method == 'GET'):
        print('GET')
        return render(request, 'form.html', {'form': forms.FilterForm()})
    if(request.method == 'POST'):
        print('POST')
        req_data = {}
        req_data['departure_airport'] = request.POST.get("departure_airport", "")
        req_data['arrival_airport'] = request.POST.get("arrival_airport", "")
        req_data['departure_time'] = request.POST.get("departure_time", "")
        req_data['arrival_time'] = request.POST.get("arrival_time", "")
        req_data['stops'] = request.POST.get("stops", None)
        req_data['duration_mins'] = request.POST.get("duration_mins", None)

        items = models.Leg.filter_leg(req_data)
        return render(request, 'form.html', {'form': forms.FilterForm(), 'list': items})


@csrf_exempt
def json_leg_filter(request):
    if(request.method == 'GET'):
        print('GET')
        return render(request, 'form.html', {'form': forms.FilterForm()})
    if(request.method == 'POST'):
        print('POST')
        body = json.loads(request.body)
        print(body)
        req_data = {}
        inputs = [
            'departure_airport',
            'arrival_airport',
            'departure_time',
            'arrival_time',
            'stops',
            'duration_mins',
        ]
        for input in inputs:
            if(input in body and body[input]) : 
                req_data[input] = body[input]

        items = models.Leg.filter_leg(req_data)

        return JsonResponse(items, safe = False)