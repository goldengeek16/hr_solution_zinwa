from django.shortcuts import render, redirect
from .models import EmployeeDetailsPermanent
from .forms import PermanentEmployeesForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

# Permanent Employees Table.
def EmployeeTablePermanent(request):
    all_permanent_employees = EmployeeDetailsPermanent.objects.all()

    page = request.GET.get('page')
    results = 1
    paginator = Paginator(all_permanent_employees, results)

    try:
        all_permanent_employees = paginator.page(page)
    except PageNotAnInteger:
        page = 1 
        all_permanent_employees = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        all_permanent_employees = paginator.page(page)
        
    leftIndex = (int(page) - 2)  
    
    if leftIndex < 1:
        leftIndex = 1
        
    rightIndex = (int(page)+3)
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1 
    
      
    custom_range = range(leftIndex, rightIndex)

    context = {'all_permanent_employees':all_permanent_employees, 'paginator':paginator, 'custom_range':custom_range }
    return render(request, 'employees/employees_per.html', context)

# Permanent Employees ADD.
def addPermanentEmployee(request):
    
    form = PermanentEmployeesForm()
    if request.method == 'POST':
        form = PermanentEmployeesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('permanent-employee-table')
    return render (request, 'employees/add_employee_form.html')
   