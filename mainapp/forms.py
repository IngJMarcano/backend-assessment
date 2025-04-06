from django import forms

class FilterForm(forms.Form):
    departure_airport = forms.CharField(required=False, label= 'Buscar por Aeropuerto de salida')
    arrival_airport = forms.CharField(required=False, label= 'Buscar por Aeropuerto de llegada')
    departure_time = forms.DateTimeField(required=False, label= 'Buscar por Dia de salida', widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))
    arrival_time = forms.DateTimeField(required=False, label= 'Buscar por Dia de llegada', widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))
    stops = forms.IntegerField(required=False, label= 'Numero de paradas')
    duration_mins = forms.IntegerField(required=False, label= 'Buscar por duracion (minutos)')
    