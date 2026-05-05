from django.shortcuts import render
from employees.models import EmployeeDetailsPermanent
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear
from datetime import datetime
import calendar

# Create your views here.


def Dashboard(request):

    return render (request, 'dashboard/dashboard.html')

def Chart1(request):
    
    all_employees_data = EmployeeDetailsPermanent.objects.all()
    context = {
        'all_employees_data':all_employees_data , 
        }
    catchment_counts = EmployeeDetailsPermanent.objects.values('catchment').annotate(
        count=Count('id')
    ).order_by('catchment')
    total_members = EmployeeDetailsPermanent.objects.count()
    return render(request, 'dashboard/charts.html', context)




def Chart(request):
    all_employees_data = EmployeeDetailsPermanent.objects.all()
    total_members = EmployeeDetailsPermanent.objects.count()
    catchment_counts = EmployeeDetailsPermanent.objects.values('catchment').annotate(
        count=Count('catchment')
    )
    gwayi_total = 0
    sanyati_total = 0
    save_total = 0
    manyame_total = 0
    mzingwane_total = 0
    runde_total = 0
    mazowe_total = 0
    
    for item in catchment_counts:
        catchment_name = item['catchment']
        count_value = item['count']
        
        if catchment_name == 'GWAYI':
            gwayi_total = count_value
        elif catchment_name == 'SANYATI':
            sanyati_total = count_value
        elif catchment_name == 'SAVE':
            save_total = count_value
        elif catchment_name == 'MANYAME':
            manyame_total = count_value
        elif catchment_name == 'MZINGWANE':
            mzingwane_total = count_value
        elif catchment_name == 'RUNDE':
            runde_total = count_value
        elif catchment_name == 'MAZOWE':
            mazowe_total = count_value
    
    
        #--------------------------------------------------FUNCTION FOR MONTHLY EMPLOYEES --------- datetime.now().year
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
    
    
    context = {
        'all_employees_data': all_employees_data,
        'total_members': total_members,
        # Individual catchment totals
        'gwayi_total': gwayi_total,
        'sanyati_total': sanyati_total,
        'save_total': save_total,
        'manyame_total': manyame_total,
        'mzingwane_total': mzingwane_total,
        'runde_total': runde_total,
        'mazowe_total': mazowe_total,
        # Dictionary of all catchment counts
        # 'catchment_dict': catchment_dict,
        # Original queryset for flexibility
        'catchment_counts': catchment_counts,
        
        #---------------------------------------------------------------------------
        
        'all_employees_data': all_employees_data,
        'total_members': all_employees_data.count(),
        
        # Individual month variables
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
    
  
    
    return render(request, 'dashboard/charts.html', context)





