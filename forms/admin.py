from django.contrib import admin
from .models import SalaryModel, LeaveModel



# Register your models here.
admin.site.register(SalaryModel)
admin.site.register(LeaveModel)
# admin.site.register(ProbationModel)