from django.contrib import admin

from .models import EmployeeDetailsContract,EmployeeDetailsPermanent,SpousesPermanent,ChildrenPermanent,Departments
from .models import MaleClothingPermanent, FemaleClothingPermanent
# Register your models here.


admin.site.register(EmployeeDetailsPermanent)
admin.site.register(EmployeeDetailsContract)
admin.site.register(SpousesPermanent)
admin.site.register(ChildrenPermanent)
admin.site.register(Departments)
admin.site.register(MaleClothingPermanent)
admin.site.register(FemaleClothingPermanent)