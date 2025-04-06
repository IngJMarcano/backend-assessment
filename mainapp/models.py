from django.db import models
from django.db.models import Q

class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    agent_rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} calificacion:{self.agent_rating}"

class Airline(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Itinerarie(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=22, decimal_places=2)
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f"Itinerario Numero:{self.id} - {self.price}$"

class Leg(models.Model):
    id = models.AutoField(primary_key=True)
    itinerarie_id = models.ForeignKey(Itinerarie, on_delete=models.CASCADE)
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport = models.CharField(max_length=3)
    arrival_airport = models.CharField(max_length=3)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    duration_mins = models.IntegerField()

    def __str__(self):
        return f"Vuelo {self.id} (Desde: {self.departure_airport} Hasta: {self.arrival_airport})"
    
    
    def filter_leg(req_data):
        query = Q()
        
        if 'departure_airport' in req_data and req_data['departure_airport']:
            query &= Q(departure_airport__icontains=req_data['departure_airport'])
        if 'arrival_airport' in req_data and req_data['arrival_airport']:
            query &= Q(arrival_airport__icontains=req_data['arrival_airport'])
        if 'departure_time' in req_data and req_data['departure_time']:
            query &= Q(departure_time__icontains=req_data['departure_time'])
        if 'arrival_time' in req_data and req_data['arrival_time']:
            query &= Q(arrival_time__icontains=req_data['arrival_time'])
        if 'stops' in req_data and req_data['stops'] is not "":
            query &= Q(stops__lte=req_data['stops'])
        if 'duration_mins' in req_data and req_data['duration_mins'] is not "":
            query &= Q(duration_mins__lte=req_data['duration_mins'])
        
        
        res = Leg.objects.filter(query)
        items = []
        for row in res:
            item = {
                "id" : row.id,
                "departure_airport" : row.departure_airport,
                "arrival_airport" : row.arrival_airport,
                "departure_time" : row.departure_time,
                "arrival_time" : row.arrival_time,
                "stops" : row.stops,
                "duration_mins" : row.duration_mins
            }
            items.append(item)
        return items
