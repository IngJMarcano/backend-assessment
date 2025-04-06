from django.contrib import admin
from . import models

class LegsList(admin.ModelAdmin):
    list_display = ['id', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'stops', 'duration_mins', 'airline_id']
    list_filter = ['airline_id', 'departure_airport', 'arrival_airport', 'duration_mins']
    search_fields = ['departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'stops', 'duration_mins']

admin.site.register(models.Agent)
admin.site.register(models.Airline)
admin.site.register(models.Itinerarie)
admin.site.register(models.Leg, LegsList)
