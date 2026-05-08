from django import forms
from .models import EmployeeDetailsPermanent, SpousesPermanent, EmployeeDocument
from django.forms import ModelForm, modelformset_factory, widgets



class PermanentEmployeesForm(ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
        input_formats=['%Y-%m-%d']
    )

    date_of_appointment = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
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
        ]

        widgets = {
            'department': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'home_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'work_physical_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(PermanentEmployeesForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in ['department']:
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
