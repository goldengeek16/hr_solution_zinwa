from django.shortcuts import render
from employees.models import EmployeeDetailsPermanent
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear
from datetime import datetime
import calendar

########## CHARTS FUNCTIONS 
from .helpers.chart_functions import get_catchment_data, monthly_employment,gender_permanent


def Chart(request):
    all_employees_data = EmployeeDetailsPermanent.objects.all()
    catchment_stats = get_catchment_data()
    monthly_employment_stats = monthly_employment()
    gender_data = gender_permanent()
   
       
    context = {
         'all_employees_data': all_employees_data,
        'total_members': catchment_stats['total_members'],
        'gwayi_total': catchment_stats['gwayi_total'],
        'sanyati_total': catchment_stats['sanyati_total'],
        'save_total': catchment_stats['save_total'],
        'manyame_total': catchment_stats['manyame_total'],
        'mzingwane_total': catchment_stats['mzingwane_total'],
        'runde_total': catchment_stats['runde_total'],
        'mazowe_total': catchment_stats['mazowe_total'],
        'catchment_counts': catchment_stats['catchment_counts'],
        'catchment_totals': catchment_stats['catchment_totals'],
        
        #---------------------------------------------------------------------------
        
        'all_employees_data': all_employees_data,
        'total_members': all_employees_data.count(),
        
        # Individual month variables
        'month_jan':monthly_employment_stats ['month_jan'],
        'month_feb': monthly_employment_stats ['month_feb'],
        'month_mar': monthly_employment_stats['month_mar'],
        'month_apr': monthly_employment_stats['month_apr'],
        'month_may': monthly_employment_stats['month_may'],
        'month_jun': monthly_employment_stats['month_jun'],
        'month_jul': monthly_employment_stats['month_jul'],
        'month_aug': monthly_employment_stats['month_aug'],
        'month_sep': monthly_employment_stats['month_sep'],
        'month_oct':monthly_employment_stats ['month_oct'],
        'month_nov': monthly_employment_stats['month_nov'],
        'month_dec': monthly_employment_stats['month_dec'],
        
        # List/dictionary for easy iteration
        'monthly_data': monthly_employment_stats['monthly_data'],
        'month_names':monthly_employment_stats ['month_names'],
        'month_counts':monthly_employment_stats ['month_counts'],
        'current_year': monthly_employment_stats['current_year'],
        
        # Optional: all years data
        'all_years_appointments': monthly_employment_stats['all_years_appointments'],
        
        #--------------------------------------------------------------
        'all_employees_data': all_employees_data,
        'total_male': gender_data ['total_male'],
        'total_female': gender_data ['total_female'],
        'total_employees': gender_data ['total_employees'],
         'male_ratio':gender_data['male_ratio'],
        'female_ratio':gender_data['female_ratio'],
    }

    return render(request, 'dashboard/charts.html', context)





