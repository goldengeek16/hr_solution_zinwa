from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('permanent-employee-table/', views.EmployeeTablePermanent, name='permanent-employee-table'),
    path('add-permanent-form/', views.addPermanentEmployee, name='add-permanent-form'),
    path('permanent-employee-view/<uuid:pk>/', views.permanentEmployeeView, name='permanent-employee-view'),
    path('edit-permanent-employee/<uuid:pk>/', views.editPermanentEmployee, name='edit-permanent-employee'),
    path('delete-permanent-employee/<uuid:pk>/', views.deletePermanentEmployee, name='delete-permanent-employee'),
    path('spouses-permanent-table/', views.spousePermanentTable, name='spouses-permanent-table'),
    path('add-spouse/', views.addSpouseView, name='add-spouse'),
    path('spouse-view/<str:pk>/' ,views.spouseView, name='spouse-view'),
    path('spouse-edit/<str:pk>/' ,views.editSpouseView , name='spouse-edit'),
    path('delete-spouse/<str:pk>/', views.deleteSpouseView, name='delete-spouse'),
    path('permanent-employee-kin', views.nextOfKinViewTable, name='permanent-employee-kin'),
    path('permanent-employee-kin-view/<str:pk>/', views.nextOfKinView, name='permanent-employee-kin-view'),
    
    
    path('export-pdf/<str:pk>/' ,views.export_pdf, name='export-pdf'),
]