from django import forms
from .models import EmployeeDetailsPermanent
from django.forms import ModelForm, widgets


#Permanent Employees Form Add
class PermanentEmployeesForm(ModelForm):
    class Meta:
        model = EmployeeDetailsPermanent
        fields = ['first_name','surname']
        widgets = {
            'departments':forms.Select()
        }

    def __init__( self, *args, **kwargs):
        super(PermanentEmployeesForm,self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input',})