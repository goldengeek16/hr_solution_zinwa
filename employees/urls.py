from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('permanent-employee-table/', views.EmployeeTablePermanent, name='permanent-employee-table'),
    path('add-permanent-form/',views.addPermanentEmployee, name='add-permanent-form'),
    path('spouses-permanent-table/', views.spousePermanentTable, name='spouses-permanent-table'),
    path('spouse-view/<str:pk>/' ,views.spouseView, name='spouse-view'),
    path('spouse-edit/<str:pk>/' ,views.editSpouseView , name='spouse-edit'),
]