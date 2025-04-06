from django.urls import path
from . import views

urlpatterns = [
    path('normal_leg_filter', views.normal_leg_filter),
    path('json_leg_filter', views.json_leg_filter)
]