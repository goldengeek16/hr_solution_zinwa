from django.contrib import admin
from django.http import HttpResponse

from .models import EmployeeDetailsContract,EmployeeDetailsPermanent,SpousesPermanent,ChildrenPermanent,Departments
from .models import MaleClothingPermanent, FemaleClothingPermanent, NextOfKinPermanent
# Register your models here.

from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter
from reportlab.platypus  import Table, TableStyle
from reportlab.lib import colors


#- --------------- --------------
from employees.handles.download_pdf import download_pdf
from employees.handles.download_csv import download_csv


admin.site.register(EmployeeDetailsPermanent)
admin.site.register(EmployeeDetailsContract)
admin.site.register(SpousesPermanent)
admin.site.register(ChildrenPermanent)
admin.site.register(Departments)
admin.site.register(MaleClothingPermanent)
admin.site.register(FemaleClothingPermanent)
admin.site.register(NextOfKinPermanent)

# - - ------------------




admin.site.add_action(download_pdf)
admin.site.add_action(download_csv)

