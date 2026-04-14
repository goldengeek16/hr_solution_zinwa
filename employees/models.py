from django.db import models
import uuid

# Create your models here.


#---------------------Permanent------------------------------
class EmployeeDetailsPermanent(models.Model):

    ec_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, 
                              choices=[
                                  ('MALE','MALE'),
                                  ('FEMALE','FEMALE'),                           
                              ])
    title = models.CharField(max_length=100, 
                             choices=[
                                  ('Mr','Mr'),
                                  ('Miss','Miss'),
                                  ('Mrs','Mrs'),                          
                              ])
    id_number = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    home_address = models.TextField(max_length=100)
    date_of_appointment = models.DateField()
    current_position = models.CharField(max_length=100)
    department = models.ManyToManyField('Departments', blank=False,null=False)
    documents = models.FileField(null=True, blank=True)
    catchment = models.CharField(max_length=100, 
                             choices=[
                                  ('SAVE','SAVE'),
                                  ('MANYAME','MANYAME'),
                                  ('MZINGWANE','MZINGWANE'),
                                    ('RUNDE','RUNDE'),
                                  ('MAZOWE','MAZOWE'),
                                  ('SANYATI','SANYATI'),
                                   ('GWAYI','GWAYI'),                        
                              ])
    grade = models.IntegerField()
    pension_fund =  models.CharField(max_length=100)
    station_cell = models.CharField(max_length=100, blank=True, null=True)
    work_physical_address = models.TextField(max_length=100, null=True, blank=True)
    employee_image = models.ImageField(null=True, blank=True)
    nssa_number = models.CharField(max_length=15, null=True, blank=True)
    drivers_license = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.first_name + self.surname + self.ec_number



class EmployeeDetailsContract(models.Model):

    ec_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, 
                              choices=[
                                  ('MALE','MALE'),
                                  ('FEMALE','FEMALE'),                           
                              ])
    title = models.CharField(max_length=100, 
                             choices=[
                                  ('Mr','Mr'),
                                  ('Miss','Miss'),
                                  ('Mrs','Mrs'),                          
                              ])
    id_number = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    home_address = models.TextField(max_length=100)
    date_of_appointment = models.DateField()
    current_position = models.CharField(max_length=100)
    department = models.ManyToManyField('Departments')
    documents = models.FileField(null=True, blank=True)
    catchment = models.CharField(max_length=100, 
                             choices=[
                                  ('SAVE','SAVE'),
                                  ('MANYAME','MANYAME'),
                                  ('MZINGWANE','MZINGWANE'),
                                    ('RUNDE','RUNDE'),
                                  ('MAZOWE','MAZOWE'),
                                  ('SANYATI','SANYATI'),
                                   ('GWAYI','GWAYI'),  
                                   ('HEAD OFFICE','HEAD OFFICE'),                      
                              ])
    grade = models.IntegerField()
    station_cell = models.CharField(max_length=100, blank=True, null=True)
    work_physical_address = models.TextField(max_length=100, null=True, blank=True)
    employee_image = models.ImageField(null=True, blank=True)
    drivers_license = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.first_name + self.surname + self.ec_number

class Departments(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200 , blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name 



class SpousesPermanent(models.Model):

    Employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete = models.SET_NULL, blank=True, null=True
    )
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100,unique=True)
    date_of_birth = models.DateField(max_length=100)
    occupation = models.CharField(max_length=100)
    date_of_marriage = models.DateField(max_length=100)
    cell_number = models.CharField(max_length=100)
    home_address = models.TextField(max_length=100)
    workplace_number = models.CharField(max_length=100, null=True, blank=True)
    workplace_address = models.CharField(max_length=100, null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
   
    def __str__(self):
        return self.first_name + self.surname 

class ChildrenPermanent(models.Model):

    Employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete = models.SET_NULL, blank=True, null=True
    )
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    birth_entry_number = models.DateField()
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.first_name + self.surname 
    
    
class NextOfKinPermanent(models.Model):

    Employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete = models.SET_NULL, blank=True, null=True
    )
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True)
    relationship = models.TextField()
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.first_name + self.surname 

class MaleClothingPermanent(models.Model):

    Employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete = models.SET_NULL, blank=True, null=True
    )
    shirt = models.CharField(max_length=10)
    trousers = models.CharField(max_length=10)
    suit = models.CharField(max_length=10)
    jacket = models.CharField(max_length=10)
    jersey = models.CharField(max_length=10)
    tshirt = models.CharField(max_length=10)
    shoes = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.Employee 
class FemaleClothingPermanent(models.Model):

    Employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete = models.SET_NULL, blank=True, null=True
    )
    shirt = models.CharField(max_length=10)
    trousers = models.CharField(max_length=10)
    suit = models.CharField(max_length=10)
    jacket = models.CharField(max_length=10)
    jersey = models.CharField(max_length=10)
    tshirt = models.CharField(max_length=10)
    shoes = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.Employee 