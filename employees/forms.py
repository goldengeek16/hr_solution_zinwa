from django import forms
from .models import ContractEmployeeDocument, EmployeeDetailsContract, EmployeeDetailsPermanent, SpousesContract, SpousesPermanent, EmployeeDocument, NextOfKinContract, NextOfKinPermanent
from django.forms import ModelForm, modelformset_factory, widgets



class PermanentEmployeesForm(ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    date_of_appointment = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = EmployeeDetailsPermanent
        fields = [
            'ec_number',
            'title',
            'first_name',
            'surname',
            'gender',
            'id_number',
            'date_of_birth',
            'nationality',
            'contact',
            'email',
            'home_address',
            'date_of_appointment',
            'current_position',
            'department',
            # 'documents',
            'catchment',
            'grade',
            'pension_fund',
            'station_cell',
            'work_physical_address',
            'employee_image',
            'nssa_number',
            'drivers_license',
            'status',
        ]

        widgets = {
            'title': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'catchment': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'home_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'work_physical_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(PermanentEmployeesForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in ['department', 'title', 'gender', 'catchment', 'status']:
                field.widget.attrs.update({'class': 'form-select'})
            elif name in ['home_address', 'work_physical_address']:
                field.widget.attrs.update({'class': 'form-textarea'})
            elif name not in ['date_of_birth', 'date_of_appointment']:
                field.widget.attrs.update({'class': 'form-input'})


class EmployeeDocumentForm(ModelForm):
    class Meta:
        model = EmployeeDocument
        fields = ['document_type', 'certificate_name', 'document_file']

        widgets = {
            'document_type': forms.Select(attrs={'class': 'form-select document-type'}),
            'certificate_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Example: Diploma in HR, Degree Certificate'
            }),
            'document_file': forms.FileInput(attrs={'class': 'form-input'}),
        }


EmployeeDocumentFormSet = modelformset_factory(
    EmployeeDocument,
    form=EmployeeDocumentForm,
    extra=1,
    can_delete=True
)

class SpousePermanentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )
    date_of_marriage = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = SpousesPermanent
        fields = [
            'Employee',
            'first_name',
            'surname',
            'id_number',
            'date_of_birth',
            'occupation',
            'date_of_marriage',
            'cell_number',
            'home_address',
            'workplace_number',
            'workplace_address',
        ]

        widgets = {
            'Employee': forms.Select(attrs={
                'class': 'form-select',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'id_number': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'date_of_marriage': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'cell_number': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'home_address': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 4,
            }),
            'workplace_number': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'workplace_address': forms.TextInput(attrs={
                'class': 'form-input',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(SpousePermanentForm, self).__init__(*args, **kwargs)
        self.fields['Employee'].required = True


class EmployeeSpouseForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )
    date_of_marriage = forms.DateField(
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = SpousesPermanent
        fields = [
            'first_name',
            'surname',
            'id_number',
            'date_of_birth',
            'occupation',
            'date_of_marriage',
            'cell_number',
            'home_address',
            'workplace_number',
            'workplace_address',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'id_number': forms.TextInput(attrs={'class': 'form-input'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'occupation': forms.TextInput(attrs={'class': 'form-input'}),
            'date_of_marriage': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'cell_number': forms.TextInput(attrs={'class': 'form-input'}),
            'home_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'workplace_number': forms.TextInput(attrs={'class': 'form-input'}),
            'workplace_address': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeSpouseForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False

class NextOfKinPermanentForm(ModelForm):
    class Meta:
        model = NextOfKinPermanent
        fields = [
            'Employee',
            'first_name',
            'surname',
            'id_number',
            'relationship',
            'contact',
        ]

        widgets = {
            'Employee': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'id_number': forms.TextInput(attrs={'class': 'form-input'}),
            'relationship': forms.TextInput(attrs={'class': 'form-input'}),
            'contact': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(NextOfKinPermanentForm, self).__init__(*args, **kwargs)
        self.fields['Employee'].required = True


class EmployeeNextOfKinForm(ModelForm):
    class Meta:
        model = NextOfKinPermanent
        fields = [
            'first_name',
            'surname',
            'id_number',
            'relationship',
            'contact',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'id_number': forms.TextInput(attrs={'class': 'form-input'}),
            'relationship': forms.TextInput(attrs={'class': 'form-input'}),
            'contact': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeNextOfKinForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False


class ContractEmployeesForm(ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    date_of_appointment = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = EmployeeDetailsContract
        fields = [
            'ec_number',
            'title',
            'first_name',
            'surname',
            'gender',
            'id_number',
            'date_of_birth',
            'nationality',
            'contact',
            'email',
            'home_address',
            'date_of_appointment',
            'current_position',
            'department',
            'catchment',
            'grade',
            'station_cell',
            'work_physical_address',
            'employee_image',
            'drivers_license',
            'status',
        ]

        widgets = {
            'title': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'catchment': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'home_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'work_physical_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(ContractEmployeesForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in ['department', 'title', 'gender', 'catchment', 'status']:
                field.widget.attrs.update({'class': 'form-select'})
            elif name in ['home_address', 'work_physical_address']:
                field.widget.attrs.update({'class': 'form-textarea'})
            elif name not in ['date_of_birth', 'date_of_appointment']:
                field.widget.attrs.update({'class': 'form-input'})


class ContractEmployeeDocumentForm(ModelForm):
    class Meta:
        model = ContractEmployeeDocument
        fields = ['document_type', 'certificate_name', 'document_file']

        widgets = {
            'document_type': forms.Select(attrs={'class': 'form-select document-type'}),
            'certificate_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Example: Contract, Diploma in HR, Degree Certificate'
            }),
            'document_file': forms.FileInput(attrs={'class': 'form-input'}),
        }


ContractEmployeeDocumentFormSet = modelformset_factory(
    ContractEmployeeDocument,
    form=ContractEmployeeDocumentForm,
    extra=1,
    can_delete=True
)


class ContractSpouseForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )
    date_of_marriage = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = SpousesContract
        fields = [
            'Employee',
            'first_name',
            'surname',
            'id_number',
            'date_of_birth',
            'occupation',
            'date_of_marriage',
            'cell_number',
            'home_address',
            'workplace_number',
            'workplace_address',
        ]

        widgets = {
            'Employee': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'id_number': forms.TextInput(attrs={'class': 'form-input'}),
            'occupation': forms.TextInput(attrs={'class': 'form-input'}),
            'cell_number': forms.TextInput(attrs={'class': 'form-input'}),
            'home_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'workplace_number': forms.TextInput(attrs={'class': 'form-input'}),
            'workplace_address': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContractSpouseForm, self).__init__(*args, **kwargs)
        self.fields['Employee'].required = True


class ContractEmployeeSpouseForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )
    date_of_marriage = forms.DateField(
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = SpousesContract
        fields = [
            'first_name',
            'surname',
            'id_number',
            'date_of_birth',
            'occupation',
            'date_of_marriage',
            'cell_number',
            'home_address',
            'workplace_number',
            'workplace_address',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'id_number': forms.TextInput(attrs={'class': 'form-input'}),
            'occupation': forms.TextInput(attrs={'class': 'form-input'}),
            'cell_number': forms.TextInput(attrs={'class': 'form-input'}),
            'home_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'workplace_number': forms.TextInput(attrs={'class': 'form-input'}),
            'workplace_address': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContractEmployeeSpouseForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False


class ContractNextOfKinForm(ModelForm):
    class Meta:
        model = NextOfKinContract
        fields = [
            'Employee',
            'first_name',
            'surname',
            'id_number',
            'relationship',
            'contact',
        ]

        widgets = {
            'Employee': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'id_number': forms.TextInput(attrs={'class': 'form-input'}),
            'relationship': forms.TextInput(attrs={'class': 'form-input'}),
            'contact': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContractNextOfKinForm, self).__init__(*args, **kwargs)
        self.fields['Employee'].required = True


class ContractEmployeeNextOfKinForm(ModelForm):
    class Meta:
        model = NextOfKinContract
        fields = [
            'first_name',
            'surname',
            'id_number',
            'relationship',
            'contact',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'id_number': forms.TextInput(attrs={'class': 'form-input'}),
            'relationship': forms.TextInput(attrs={'class': 'form-input'}),
            'contact': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContractEmployeeNextOfKinForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False
