from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('chart-catchments/', views.Chart, name='chart-catchments'),
    
]