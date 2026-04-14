from django.db import models
from employees.models import EmployeeDetailsPermanent
import uuid
# Create your models here.


                 # SALARY MODEL
class SalaryModel(models.Model):
    employee = models.ForeignKey(EmployeeDetailsPermanent, on_delete=models.CASCADE, null=False, blank=False)
    name_of_bank = models.CharField(max_length=200, null=False, blank=False)
    branch = models.CharField(max_length=200, null=False, blank=False)
    account_number = models.CharField(max_length=200, null=False,blank=False)
    date = models.DateField(max_length=200, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False, primary_key=True)
    
    def __str__(self):
        return self.name_of_bank + "-" + self.account_number
    
    
                # LEAVE MODEL
class LeaveModel(models.Model):
    #employee = models.ForeignKey(EmployeeDetailsPermanent, on_delete=models.CASCADE, null=False, blank=False)
    # date_of_engagement = models.DateField(max_length=200, blank=False, null=False)
    # leave_type = models.CharField(max_length=200, blank=False, null=False)
    # leave_entitlement = models.CharField(max_length=200, blank=False, null=False)
    # start_date = models.DateField(max_length=200, blank=False, null=False)
    # end_date = models.DateField(max_length=200, blank=False, null=False)
    # leave_entitlement_granted = models.CharField(max_length=200, blank=True, null=True)
    # accrual_per_year = models.CharField(max_length=200, blank=False, null=False)
    # leave_start_date = models.DateField(max_length=200, blank=False, null=False)
    # leave_end_date = models.DateField(max_length=200, blank=False, null=False)
    # number_of_days_taken = models.CharField(max_length=200, blank=False, null=False)
    balance = models.CharField(max_length=200, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False, primary_key=True)
    
    # def __str__(self):
    #     return self.balance
    
#                  # PROBATION MODEL

# class ProbationModel(models.Model):
#     period_start = models.DateField(max_length=200, blank=False, null=False)
#     period_end = models.DateField(max_length=200, blank=False, null=False)
#     name_of_probationer = models.CharField(max_length=200, blank=False, null=False)
#     job_title = models.CharField(max_length=200, blank=False, null=False)
#     catchment = models.CharField(max_length=200,
#                                  choices=[
#                                   ('SAVE','SAVE'),
#                                   ('MANYAME','MANYAME'),
#                                   ('MZINGWANE','MZINGWANE'),
#                                     ('RUNDE','RUNDE'),
#                                   ('MAZOWE','MAZOWE'),
#                                   ('SANYATI','SANYATI'),
#                                    ('GWAYI','GWAYI'),  
#                                    ('HEAD OFFICE','HEAD OFFICE'),                      
#                               ])
#     #department = models.ManyToManyField(Departments, blank=True, null=True, max_length=200)
#     station = models.CharField(max_length=200, blank=False,null=True)
#     date = models.DateField(max_length=200, null=False, blank=False)
#     supervisor_assessment = models.CharField(max_length=200, blank=False, null=False)
#     quality_of_work = models.CharField(max_length=100, null=False, blank=False)
#     motivation = models.CharField(max_length=100, null=False, blank=False)
#     panctuality = models.CharField(max_length=100, blank=False, null=False)
#     adaptability = models.CharField(max_length=100, blank=False, null=False)
#     communication = models.CharField(max_length=100, blank=False, null=False)
#     attitude_towards_workmates = models.CharField(max_length=100, blank=False, null=False)
#     comment = models.TextField = models.CharField(max_length=100,blank=False,null=False)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False, primary_key=True)