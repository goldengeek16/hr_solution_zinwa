from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('permanent-employee-table/', views.EmployeeTablePermanent, name='permanent-employee-table'),
    path('add-permanent-form/',views.addPermanentEmployee, name='add-permanent-form'),
]