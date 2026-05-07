from django.shortcuts import render
from employees.models import EmployeeDetailsPermanent
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear
from datetime import datetime
import calendar


def get_catchment_data():
   
    total_members = EmployeeDetailsPermanent.objects.count()
    catchment_counts = EmployeeDetailsPermanent.objects.values('catchment').annotate(
        count=Count('catchment')
    )
    
    # Initialize catchment totals
    catchment_totals = {
        'GWAYI': 0,
        'SANYATI': 0,
        'SAVE': 0,
        'MANYAME': 0,
        'MZINGWANE': 0,
        'RUNDE': 0,
        'MAZOWE': 0,
    }
    
    # Populate totals from query results
    for item in catchment_counts:
        catchment_name = item['catchment']
        count_value = item['count']
        
        if catchment_name in catchment_totals:
            catchment_totals[catchment_name] = count_value
    
    # Return all data in a structured format
    return {
        'total_members': total_members,
        'catchment_counts': catchment_counts,
        'catchment_totals': catchment_totals,
        # Individual variables for template compatibility
        'gwayi_total': catchment_totals.get('GWAYI', 0),
        'sanyati_total': catchment_totals.get('SANYATI', 0),
        'save_total': catchment_totals.get('SAVE', 0),
        'manyame_total': catchment_totals.get('MANYAME', 0),
        'mzingwane_total': catchment_totals.get('MZINGWANE', 0),
        'runde_total': catchment_totals.get('RUNDE', 0),
        'mazowe_total': catchment_totals.get('MAZOWE', 0),
    }


def get_catchment_totals_dict():
    """
        dict: { 'GWAYI': 10, 'SANYATI': 5, ... }
    """
    catchment_counts = EmployeeDetailsPermanent.objects.values('catchment').annotate(
        count=Count('catchment')
    )
    
    return {item['catchment']: item['count'] for item in catchment_counts}


def get_catchment_list_with_percentages():
   
    total = EmployeeDetailsPermanent.objects.count()
    catchment_counts = EmployeeDetailsPermanent.objects.values('catchment').annotate(
        count=Count('catchment')
    )
    
    catchment_list = []
    for item in catchment_counts:
        catchment_list.append({
            'name': item['catchment'],
            'count': item['count'],
            'percentage': (item['count'] / total * 100) if total > 0 else 0
        })
    
    return catchment_list


def monthly_employment():
    current_year = datetime.now().year
    
    monthly_appointments = EmployeeDetailsPermanent.objects.filter(
        date_of_appointment__year=current_year
    ).annotate(
        month=ExtractMonth('date_of_appointment')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')
    
    # Initialize counters for each month (1-12)
    month_counts = {
        1: 0,  # January
        2: 0,  # February
        3: 0,  # March
        4: 0,  # April
        5: 0,  # May
        6: 0,  # June
        7: 0,  # July
        8: 0,  # August
        9: 0,  # September
        10: 0, # October
        11: 0, # November
        12: 0, # December
    }
    
    # # Fill in the actual counts
    for item in monthly_appointments:
        month_counts[item['month']] = item['count']
    
    # # Create individual month variables
    month_jan = month_counts[1]
    month_feb = month_counts[2]
    month_mar = month_counts[3]
    month_apr = month_counts[4]
    month_may = month_counts[5]
    month_jun = month_counts[6]
    month_jul = month_counts[7]
    month_aug = month_counts[8]
    month_sep = month_counts[9]
    month_oct = month_counts[10]
    month_nov = month_counts[11]
    month_dec = month_counts[12]
    
    # Alternative: Create a list for easy iteration in template
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    monthly_data = [
        {'month': 'January', 'count': month_jan},
        {'month': 'February', 'count': month_feb},
        {'month': 'March', 'count': month_mar},
        {'month': 'April', 'count': month_apr},
        {'month': 'May', 'count': month_may},
        {'month': 'June', 'count': month_jun},
        {'month': 'July', 'count': month_jul},
        {'month': 'August', 'count': month_aug},
        {'month': 'September', 'count': month_sep},
        {'month': 'October', 'count': month_oct},
        {'month': 'November', 'count': month_nov},
        {'month': 'December', 'count': month_dec},
    ]
    
    # Get appointments for all years (optional)
    all_years_appointments = EmployeeDetailsPermanent.objects.annotate(
        year=ExtractYear('date_of_appointment'),
        month=ExtractMonth('date_of_appointment')
    ).values('year', 'month').annotate(
        count=Count('id')
    ).order_by('year', 'month')
    
    return {
        'month_jan': month_jan,
        'month_feb': month_feb,
        'month_mar': month_mar,
        'month_apr': month_apr,
        'month_may': month_may,
        'month_jun': month_jun,
        'month_jul': month_jul,
        'month_aug': month_aug,
        'month_sep': month_sep,
        'month_oct': month_oct,
        'month_nov': month_nov,
        'month_dec': month_dec,
        
        # List/dictionary for easy iteration
        'monthly_data': monthly_data,
        'month_names': month_names,
        'month_counts': month_counts,
        'current_year': current_year,
        
        # Optional: all years data
        'all_years_appointments': all_years_appointments,
    }
    
def gender_permanent():
    gender_stats = EmployeeDetailsPermanent.objects.values('gender').annotate(
        count=Count('gender')
    )
    
    # Initialize counts
    total_male = 0
    total_female = 0
    
    for stat in gender_stats:
        if stat['gender'] == 'MALE':
            total_male = stat['count']
        elif stat['gender'] == 'FEMALE':
            total_female = stat['count']
    
    total_employees = total_male + total_female
    if total_employees > 0:
        male_ratio = int((total_male/total_employees) * 100)
        female_ratio = int((total_female/total_employees) * 100)
    else:
        male_ratio = 0
        female_ratio = 0
    
    return {
        'total_male':total_male,
        'total_female': total_female,
        'total_employees':total_employees,
        'male_ratio':male_ratio,
        'female_ratio':female_ratio,
        
        
    }