from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeDetailsPermanent , SpousesPermanent, NextOfKinPermanent, EmployeeDocument
from .forms import EmployeeDocumentFormSet, PermanentEmployeesForm , SpousePermanentForm
from django.db.models import Count
import uuid 


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

# Permanent Employees Table.

def EmployeeTablePermanent(request):
    employee_list = EmployeeDetailsPermanent.objects.all().order_by('surname', 'first_name')

    catchment_counts = EmployeeDetailsPermanent.objects.values('catchment').annotate(
        count=Count('id')
    ).order_by('catchment')

    total_members = EmployeeDetailsPermanent.objects.count()

    page = request.GET.get('page')
    results = 10
    paginator = Paginator(employee_list, results)

    try:
        all_permanent_employees = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        all_permanent_employees = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        all_permanent_employees = paginator.page(page)

    leftIndex = int(page) - 2

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 3

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    context = {
        'all_permanent_employees': all_permanent_employees,
        'paginator': paginator,
        'custom_range': custom_range,
        'catchment_counts': catchment_counts,
        'total_members': total_members,
    }

    return render(request, 'employees/permanentEmployeesTable.html', context)


def addPermanentEmployee(request):
    form = PermanentEmployeesForm()
    document_formset = EmployeeDocumentFormSet(
        queryset=EmployeeDocument.objects.none(),
        prefix='documents'
    )
    spouse_form = SpousePermanentForm(prefix='spouse')

    if request.method == 'POST':
        form = PermanentEmployeesForm(request.POST, request.FILES)
        document_formset = EmployeeDocumentFormSet(
            request.POST,
            request.FILES,
            queryset=EmployeeDocument.objects.none(),
            prefix='documents'
        )
        spouse_form = SpousePermanentForm(request.POST, prefix='spouse')

        spouse_has_data = any(
            request.POST.get(f'spouse-{field}')
            for field in spouse_form.fields
        )

        forms_are_valid = form.is_valid() and document_formset.is_valid()

        if spouse_has_data:
            forms_are_valid = forms_are_valid and spouse_form.is_valid()

        if forms_are_valid:
            employee = form.save()

            for doc_form in document_formset:
                if doc_form.cleaned_data and not doc_form.cleaned_data.get('DELETE'):
                    document = doc_form.save(commit=False)
                    document.employee = employee
                    document.save()

            if spouse_has_data:
                spouse = spouse_form.save(commit=False)
                spouse.Employee = employee
                spouse.save()

            return redirect('permanent-employee-table')

    context = {
        'form': form,
        'document_formset': document_formset,
        'spouse_form': spouse_form,
    }

    return render(request, 'employees/add_permemployee.html', context)


def editPermanentEmployee(request, pk):
    employee = get_object_or_404(EmployeeDetailsPermanent, id=pk)
    spouse = SpousesPermanent.objects.filter(Employee=employee).first()

    form = PermanentEmployeesForm(instance=employee)
    document_formset = EmployeeDocumentFormSet(
        queryset=EmployeeDocument.objects.filter(employee=employee),
        prefix='documents'
    )
    spouse_form = SpousePermanentForm(instance=spouse, prefix='spouse')

    if request.method == 'POST':
        form = PermanentEmployeesForm(request.POST, request.FILES, instance=employee)
        document_formset = EmployeeDocumentFormSet(
            request.POST,
            request.FILES,
            queryset=EmployeeDocument.objects.filter(employee=employee),
            prefix='documents'
        )
        spouse_form = SpousePermanentForm(request.POST, instance=spouse, prefix='spouse')

        spouse_has_data = any(
            request.POST.get(f'spouse-{field}')
            for field in spouse_form.fields
        )

        forms_are_valid = form.is_valid() and document_formset.is_valid()

        if spouse_has_data:
            forms_are_valid = forms_are_valid and spouse_form.is_valid()

        if forms_are_valid:
            employee = form.save()

            for doc_form in document_formset:
                if doc_form.cleaned_data:
                    if doc_form.cleaned_data.get('DELETE') and doc_form.instance.id:
                        doc_form.instance.delete()
                    elif doc_form.cleaned_data.get('document_file'):
                        document = doc_form.save(commit=False)
                        document.employee = employee
                        document.save()

            if spouse_has_data:
                spouse_record = spouse_form.save(commit=False)
                spouse_record.Employee = employee
                spouse_record.save()

            return redirect('permanent-employee-table')

    context = {
        'form': form,
        'employee': employee,
        'document_formset': document_formset,
        'spouse_form': spouse_form,
    }

    return render(request, 'employees/edit_permemployee.html', context)


def permanentEmployeeView(request, pk):
    employee = get_object_or_404(EmployeeDetailsPermanent, id=pk)
    documents = EmployeeDocument.objects.filter(employee=employee)
    spouses = SpousesPermanent.objects.filter(Employee=employee)

    context = {
        'employee': employee,
        'documents': documents,
        'spouses': spouses,
    }

    return render(request, 'employees/view_permemployee.html', context)

def deletePermanentEmployee(request, pk):
    employee = get_object_or_404(EmployeeDetailsPermanent, id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('permanent-employee-table')

    context = {
        'employee': employee,
    }

    return render(request, 'employees/delete_permemployee.html', context)

#-------------------------------SPOUSES-------------------------------------------------------------------------------------------------------------

#SPOUSETABLE

def spousePermanentTable(request):
    spouses = SpousesPermanent.objects.all()
    context = { 'spouses':spouses,}

    return render (request, 'employees/spousesTable.html', context)

#SPOUSEVIEW

def spouseView(request,pk):

    spouse_view = get_object_or_404(SpousesPermanent, id=pk)
    #context = {'spouse_view' :spouse_view}
    return render(request, 'employees/spouses_view.html', {'spouse_view':spouse_view})

#ADDSPOUSE

def addSpouseView(request):
    form = SpousePermanentForm()

    if request.method == 'POST':
        form = SpousePermanentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('spouses-permanent-table')
        else:
            print(form.errors)

    context = {
        'form': form,
    }

    return render(request, 'employees/add_spouse.html', context)

#EDITSPOUSE

def editSpouseView(request, pk):
    edit_spouse = get_object_or_404(SpousesPermanent, id=pk)

    if request.method == 'POST':
        form = SpousePermanentForm(request.POST, request.FILES, instance=edit_spouse)

        if form.is_valid():
            form.save()
            return redirect('spouses-permanent-table')
    else:
        form = SpousePermanentForm(instance=edit_spouse)

    context = {
        'form': form,
        'edit_spouse': edit_spouse,
    }

    return render(request, 'employees/edit_spouse.html', context)

#DELETESPOUSE

def deleteSpouseView(request, pk):
    spouse = get_object_or_404(SpousesPermanent, id=pk)

    if request.method == 'POST':
        spouse.delete()
        return redirect('spouses-permanent-table')

    context = {
        'spouse': spouse,
    }

    return render(request, 'employees/delete_spouse.html', context)

#-------------------------------NEXT OF KIN ------------------
# view table

def nextOfKinViewTable(request):
    all_nextofkin = NextOfKinPermanent.objects.all()
    context = {'all_nextofkin': all_nextofkin}
    
    return render(request, 'employees/next_of_kin_table.html' , context)

def nextOfKinView(request,pk):
    nextofkin_view = NextOfKinPermanent.objects.get(id=pk)
    context = {'nextofkin_view':nextofkin_view}
    
    return render(request, 'employees/next_of_kin_view.html', context)