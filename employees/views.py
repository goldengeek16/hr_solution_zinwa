from django.shortcuts import render, redirect, get_object_or_404

from employees.forms import ContractEmployeeDocumentFormSet, ContractEmployeeNextOfKinForm, ContractEmployeeSpouseForm, ContractEmployeesForm, ContractNextOfKinForm, ContractSpouseForm, EmployeeDocumentFormSet, EmployeeNextOfKinForm, EmployeeSpouseForm, NextOfKinPermanentForm, PermanentEmployeesForm, SpousePermanentForm
from .models import ContractEmployeeDocument, EmployeeDetailsContract, EmployeeDetailsPermanent, SpousesContract, SpousesPermanent, NextOfKinContract, NextOfKinPermanent, EmployeeDocument
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
    spouse_form = EmployeeSpouseForm(prefix='spouse')
    nextofkin_form = EmployeeNextOfKinForm(prefix='kin')

    if request.method == 'POST':
        form = PermanentEmployeesForm(request.POST, request.FILES)
        document_formset = EmployeeDocumentFormSet(
            request.POST,
            request.FILES,
            queryset=EmployeeDocument.objects.none(),
            prefix='documents'
        )
        spouse_form = EmployeeSpouseForm(request.POST, prefix='spouse')
        nextofkin_form = EmployeeNextOfKinForm(request.POST, prefix='kin')

        spouse_has_data = any(
            request.POST.get(f'spouse-{field}')
            for field in spouse_form.fields
        )
        kin_has_data = any(
            request.POST.get(f'kin-{field}')
            for field in nextofkin_form.fields
        )

        forms_are_valid = form.is_valid() and document_formset.is_valid()

        if spouse_has_data:
            forms_are_valid = forms_are_valid and spouse_form.is_valid()
        if kin_has_data:
            forms_are_valid = forms_are_valid and nextofkin_form.is_valid()

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

            if kin_has_data:
                nextofkin = nextofkin_form.save(commit=False)
                nextofkin.Employee = employee
                nextofkin.save()

            return redirect('permanent-employee-table')

    context = {
        'form': form,
        'document_formset': document_formset,
        'spouse_form': spouse_form,
        'nextofkin_form': nextofkin_form,
    }

    return render(request, 'employees/add_permemployee.html', context)


def editPermanentEmployee(request, pk):
    employee = get_object_or_404(EmployeeDetailsPermanent, id=pk)
    spouse = SpousesPermanent.objects.filter(Employee=employee).first()
    nextofkin = NextOfKinPermanent.objects.filter(Employee=employee).first()

    form = PermanentEmployeesForm(instance=employee)
    document_formset = EmployeeDocumentFormSet(
        queryset=EmployeeDocument.objects.filter(employee=employee),
        prefix='documents'
    )
    spouse_form = EmployeeSpouseForm(instance=spouse, prefix='spouse')
    nextofkin_form = EmployeeNextOfKinForm(instance=nextofkin, prefix='kin')

    if request.method == 'POST':
        form = PermanentEmployeesForm(request.POST, request.FILES, instance=employee)
        document_formset = EmployeeDocumentFormSet(
            request.POST,
            request.FILES,
            queryset=EmployeeDocument.objects.filter(employee=employee),
            prefix='documents'
        )
        spouse_form = EmployeeSpouseForm(request.POST, instance=spouse, prefix='spouse')
        nextofkin_form = EmployeeNextOfKinForm(request.POST, instance=nextofkin, prefix='kin')

        spouse_has_data = any(
            request.POST.get(f'spouse-{field}')
            for field in spouse_form.fields
        )
        kin_has_data = any(
            request.POST.get(f'kin-{field}')
            for field in nextofkin_form.fields
        )

        forms_are_valid = form.is_valid() and document_formset.is_valid()

        if spouse_has_data:
            forms_are_valid = forms_are_valid and spouse_form.is_valid()
        if kin_has_data:
            forms_are_valid = forms_are_valid and nextofkin_form.is_valid()

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

            if kin_has_data:
                nextofkin_record = nextofkin_form.save(commit=False)
                nextofkin_record.Employee = employee
                nextofkin_record.save()

            return redirect('permanent-employee-table')

    context = {
        'form': form,
        'employee': employee,
        'document_formset': document_formset,
        'spouse_form': spouse_form,
        'nextofkin_form': nextofkin_form,
    }

    return render(request, 'employees/edit_permemployee.html', context)


def permanentEmployeeView(request, pk):
    employee = get_object_or_404(EmployeeDetailsPermanent, id=pk)
    documents = EmployeeDocument.objects.filter(employee=employee)
    spouses = SpousesPermanent.objects.filter(Employee=employee)
    nextofkins = NextOfKinPermanent.objects.filter(Employee=employee)

    context = {
        'employee': employee,
        'documents': documents,
        'spouses': spouses,
        'nextofkins': nextofkins,
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


#-------------------------------CONTRACT EMPLOYEES--------------------------------------------------------------------------------------------------

def contractEmployeeTable(request):
    employee_list = EmployeeDetailsContract.objects.all().order_by('surname', 'first_name')

    catchment_counts = EmployeeDetailsContract.objects.values('catchment').annotate(
        count=Count('id')
    ).order_by('catchment')

    total_members = EmployeeDetailsContract.objects.count()

    page = request.GET.get('page')
    results = 10
    paginator = Paginator(employee_list, results)

    try:
        all_contract_employees = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        all_contract_employees = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        all_contract_employees = paginator.page(page)

    leftIndex = int(page) - 2

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 3

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    context = {
        'all_contract_employees': all_contract_employees,
        'paginator': paginator,
        'custom_range': custom_range,
        'catchment_counts': catchment_counts,
        'total_members': total_members,
    }

    return render(request, 'employees/contractEmployeesTable.html', context)


def addContractEmployee(request):
    form = ContractEmployeesForm()
    document_formset = ContractEmployeeDocumentFormSet(
        queryset=ContractEmployeeDocument.objects.none(),
        prefix='documents'
    )
    spouse_form = ContractEmployeeSpouseForm(prefix='spouse')
    nextofkin_form = ContractEmployeeNextOfKinForm(prefix='kin')

    if request.method == 'POST':
        form = ContractEmployeesForm(request.POST, request.FILES)
        document_formset = ContractEmployeeDocumentFormSet(
            request.POST,
            request.FILES,
            queryset=ContractEmployeeDocument.objects.none(),
            prefix='documents'
        )
        spouse_form = ContractEmployeeSpouseForm(request.POST, prefix='spouse')
        nextofkin_form = ContractEmployeeNextOfKinForm(request.POST, prefix='kin')

        spouse_has_data = any(
            request.POST.get(f'spouse-{field}')
            for field in spouse_form.fields
        )
        kin_has_data = any(
            request.POST.get(f'kin-{field}')
            for field in nextofkin_form.fields
        )

        forms_are_valid = form.is_valid() and document_formset.is_valid()

        if spouse_has_data:
            forms_are_valid = forms_are_valid and spouse_form.is_valid()
        if kin_has_data:
            forms_are_valid = forms_are_valid and nextofkin_form.is_valid()

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

            if kin_has_data:
                nextofkin = nextofkin_form.save(commit=False)
                nextofkin.Employee = employee
                nextofkin.save()

            return redirect('contract-employee-table')

    context = {
        'form': form,
        'document_formset': document_formset,
        'spouse_form': spouse_form,
        'nextofkin_form': nextofkin_form,
    }

    return render(request, 'employees/add_contractemployee.html', context)


def contractEmployeeView(request, pk):
    employee = get_object_or_404(EmployeeDetailsContract, id=pk)
    documents = ContractEmployeeDocument.objects.filter(employee=employee)
    spouses = SpousesContract.objects.filter(Employee=employee)
    nextofkins = NextOfKinContract.objects.filter(Employee=employee)

    context = {
        'employee': employee,
        'documents': documents,
        'spouses': spouses,
        'nextofkins': nextofkins,
    }

    return render(request, 'employees/view_contractemployee.html', context)


def editContractEmployee(request, pk):
    employee = get_object_or_404(EmployeeDetailsContract, id=pk)
    spouse = SpousesContract.objects.filter(Employee=employee).first()
    nextofkin = NextOfKinContract.objects.filter(Employee=employee).first()

    form = ContractEmployeesForm(instance=employee)
    document_formset = ContractEmployeeDocumentFormSet(
        queryset=ContractEmployeeDocument.objects.filter(employee=employee),
        prefix='documents'
    )
    spouse_form = ContractEmployeeSpouseForm(instance=spouse, prefix='spouse')
    nextofkin_form = ContractEmployeeNextOfKinForm(instance=nextofkin, prefix='kin')

    if request.method == 'POST':
        form = ContractEmployeesForm(request.POST, request.FILES, instance=employee)
        document_formset = ContractEmployeeDocumentFormSet(
            request.POST,
            request.FILES,
            queryset=ContractEmployeeDocument.objects.filter(employee=employee),
            prefix='documents'
        )
        spouse_form = ContractEmployeeSpouseForm(request.POST, instance=spouse, prefix='spouse')
        nextofkin_form = ContractEmployeeNextOfKinForm(request.POST, instance=nextofkin, prefix='kin')

        spouse_has_data = any(
            request.POST.get(f'spouse-{field}')
            for field in spouse_form.fields
        )
        kin_has_data = any(
            request.POST.get(f'kin-{field}')
            for field in nextofkin_form.fields
        )

        forms_are_valid = form.is_valid() and document_formset.is_valid()

        if spouse_has_data:
            forms_are_valid = forms_are_valid and spouse_form.is_valid()
        if kin_has_data:
            forms_are_valid = forms_are_valid and nextofkin_form.is_valid()

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

            if kin_has_data:
                nextofkin_record = nextofkin_form.save(commit=False)
                nextofkin_record.Employee = employee
                nextofkin_record.save()

            return redirect('contract-employee-table')

    context = {
        'form': form,
        'employee': employee,
        'document_formset': document_formset,
        'spouse_form': spouse_form,
        'nextofkin_form': nextofkin_form,
    }

    return render(request, 'employees/edit_contractemployee.html', context)


def deleteContractEmployee(request, pk):
    employee = get_object_or_404(EmployeeDetailsContract, id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('contract-employee-table')

    context = {
        'employee': employee,
    }

    return render(request, 'employees/delete_contractemployee.html', context)

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
    all_nextofkin = NextOfKinPermanent.objects.all().order_by('first_name')

    context = {
        'all_nextofkin': all_nextofkin,
    }

    return render(request, 'employees/next_of_kin_table.html', context)


def addNextOfKinView(request):
    form = NextOfKinPermanentForm()

    if request.method == 'POST':
        form = NextOfKinPermanentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('permanent-employee-kin')

    context = {
        'form': form,
    }

    return render(request, 'employees/add_next_of_kin.html', context)


def nextOfKinView(request, pk):
    nextofkin_view = get_object_or_404(NextOfKinPermanent, id=pk)

    context = {
        'nextofkin_view': nextofkin_view,
    }

    return render(request, 'employees/next_of_kin_view.html', context)


def editNextOfKinView(request, pk):
    nextofkin = get_object_or_404(NextOfKinPermanent, id=pk)

    if request.method == 'POST':
        form = NextOfKinPermanentForm(request.POST, instance=nextofkin)

        if form.is_valid():
            form.save()
            return redirect('permanent-employee-kin')
    else:
        form = NextOfKinPermanentForm(instance=nextofkin)

    context = {
        'form': form,
        'nextofkin': nextofkin,
    }

    return render(request, 'employees/edit_next_of_kin.html', context)


def deleteNextOfKinView(request, pk):
    nextofkin = get_object_or_404(NextOfKinPermanent, id=pk)

    if request.method == 'POST':
        nextofkin.delete()
        return redirect('permanent-employee-kin')

    context = {
        'nextofkin': nextofkin,
    }

    return render(request, 'employees/delete_next_of_kin.html', context)


#-------------------------------CONTRACT SPOUSES----------------------------------------------------------------------------------------------------

def contractSpouseTable(request):
    spouses = SpousesContract.objects.all().order_by('first_name')

    context = {
        'spouses': spouses,
    }

    return render(request, 'employees/contractSpousesTable.html', context)


def contractSpouseView(request, pk):
    spouse_view = get_object_or_404(SpousesContract, id=pk)

    return render(request, 'employees/contract_spouses_view.html', {
        'spouse_view': spouse_view,
    })


def addContractSpouseView(request):
    form = ContractSpouseForm()

    if request.method == 'POST':
        form = ContractSpouseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('contract-spouses-table')

    context = {
        'form': form,
    }

    return render(request, 'employees/add_contract_spouse.html', context)


def editContractSpouseView(request, pk):
    edit_spouse = get_object_or_404(SpousesContract, id=pk)

    if request.method == 'POST':
        form = ContractSpouseForm(request.POST, request.FILES, instance=edit_spouse)

        if form.is_valid():
            form.save()
            return redirect('contract-spouses-table')
    else:
        form = ContractSpouseForm(instance=edit_spouse)

    context = {
        'form': form,
        'edit_spouse': edit_spouse,
    }

    return render(request, 'employees/edit_contract_spouse.html', context)


def deleteContractSpouseView(request, pk):
    spouse = get_object_or_404(SpousesContract, id=pk)

    if request.method == 'POST':
        spouse.delete()
        return redirect('contract-spouses-table')

    context = {
        'spouse': spouse,
    }

    return render(request, 'employees/delete_contract_spouse.html', context)


#-------------------------------CONTRACT NEXT OF KIN------------------------------------------------------------------------------------------------

def contractNextOfKinTable(request):
    all_nextofkin = NextOfKinContract.objects.all().order_by('first_name')

    context = {
        'all_nextofkin': all_nextofkin,
    }

    return render(request, 'employees/contract_next_of_kin_table.html', context)


def addContractNextOfKinView(request):
    form = ContractNextOfKinForm()

    if request.method == 'POST':
        form = ContractNextOfKinForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contract-employee-kin')

    context = {
        'form': form,
    }

    return render(request, 'employees/add_contract_next_of_kin.html', context)


def contractNextOfKinView(request, pk):
    nextofkin_view = get_object_or_404(NextOfKinContract, id=pk)

    context = {
        'nextofkin_view': nextofkin_view,
    }

    return render(request, 'employees/contract_next_of_kin_view.html', context)


def editContractNextOfKinView(request, pk):
    nextofkin = get_object_or_404(NextOfKinContract, id=pk)

    if request.method == 'POST':
        form = ContractNextOfKinForm(request.POST, instance=nextofkin)

        if form.is_valid():
            form.save()
            return redirect('contract-employee-kin')
    else:
        form = ContractNextOfKinForm(instance=nextofkin)

    context = {
        'form': form,
        'nextofkin': nextofkin,
    }

    return render(request, 'employees/edit_contract_next_of_kin.html', context)


def deleteContractNextOfKinView(request, pk):
    nextofkin = get_object_or_404(NextOfKinContract, id=pk)

    if request.method == 'POST':
        nextofkin.delete()
        return redirect('contract-employee-kin')

    context = {
        'nextofkin': nextofkin,
    }

    return render(request, 'employees/delete_contract_next_of_kin.html', context)
