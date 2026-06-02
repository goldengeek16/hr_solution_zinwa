from django.db import models
import uuid

# Create your models here.


#---------------------Permanent------------------------------
class EmployeeDetailsPermanent(models.Model):
    EMPLOYEE_STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('ON_LEAVE', 'On Leave'),
        ('RETIRED', 'Retired'),
        ('TERMINATED', 'Terminated'),
        ('SUSPENDED', 'Suspended'),
    ]

    ec_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    ])
    title = models.CharField(max_length=100, choices=[
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
    ])
    id_number = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    home_address = models.TextField(max_length=100)
    date_of_appointment = models.DateField()
    current_position = models.CharField(max_length=100)
    department = models.ManyToManyField('Departments', blank=False)
    documents = models.FileField(null=True, blank=True)
    catchment = models.CharField(max_length=100, choices=[
        ('SAVE', 'SAVE'),
        ('MANYAME', 'MANYAME'),
        ('MZINGWANE', 'MZINGWANE'),
        ('RUNDE', 'RUNDE'),
        ('MAZOWE', 'MAZOWE'),
        ('SANYATI', 'SANYATI'),
        ('GWAYI', 'GWAYI'),
    ])
    grade = models.IntegerField()
    pension_fund = models.CharField(max_length=100)
    station_cell = models.CharField(max_length=100, blank=True, null=True)
    work_physical_address = models.TextField(max_length=100, null=True, blank=True)
    employee_image = models.ImageField(null=True, blank=True)
    nssa_number = models.CharField(max_length=15, null=True, blank=True)
    drivers_license = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=EMPLOYEE_STATUS_CHOICES,
        default='ACTIVE'
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.surname} {self.ec_number}"


#---------------------DOCUMENTS------------------------------
class EmployeeDocument(models.Model):
    DOCUMENT_TYPES = [
        ('BIRTH_CERTIFICATE', 'Birth Certificate'),
        ('COPY_OF_ID', 'Copy of ID'),
        ('POLICE_CLEARANCE', 'Police Clearance'),
        ('ACADEMIC', 'Academic Document'),
        ('OTHER', 'Other'),
    ]

    employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete=models.CASCADE,
        related_name='employee_documents'
    )
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    certificate_name = models.CharField(max_length=150, blank=True, null=True)
    document_file = models.FileField(upload_to='employee_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.document_type == 'ACADEMIC' and self.certificate_name:
            return self.certificate_name

        return self.get_document_type_display()




class EmployeeDetailsContract(models.Model):
    EMPLOYEE_STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('ON_LEAVE', 'On Leave'),
        ('RETIRED', 'Retired'),
        ('TERMINATED', 'Terminated'),
        ('SUSPENDED', 'Suspended'),
        ('CONTRACT_ENDED', 'Contract Ended'),
    ]

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
                                  ('Ms','Ms'),
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
    status = models.CharField(
        max_length=20,
        choices=EMPLOYEE_STATUS_CHOICES,
        default='ACTIVE'
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False, primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.surname} {self.ec_number}"


class ContractEmployeeDocument(models.Model):
    DOCUMENT_TYPES = [
        ('BIRTH_CERTIFICATE', 'Birth Certificate'),
        ('COPY_OF_ID', 'Copy of ID'),
        ('POLICE_CLEARANCE', 'Police Clearance'),
        ('ACADEMIC', 'Academic Document'),
        ('CONTRACT', 'Contract Document'),
        ('OTHER', 'Other'),
    ]

    employee = models.ForeignKey(
        EmployeeDetailsContract,
        on_delete=models.CASCADE,
        related_name='contract_employee_documents'
    )
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    certificate_name = models.CharField(max_length=150, blank=True, null=True)
    document_file = models.FileField(upload_to='contract_employee_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.document_type == 'ACADEMIC' and self.certificate_name:
            return self.certificate_name

        return self.get_document_type_display()

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
        on_delete=models.CASCADE, blank=True, null=True
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
        return f"{self.first_name} {self.surname}"


class SpousesContract(models.Model):
    Employee = models.ForeignKey(
        EmployeeDetailsContract,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField(max_length=100)
    occupation = models.CharField(max_length=100)
    date_of_marriage = models.DateField(max_length=100)
    cell_number = models.CharField(max_length=100)
    home_address = models.TextField(max_length=100)
    workplace_number = models.CharField(max_length=100, null=True, blank=True)
    workplace_address = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

class ChildrenPermanent(models.Model):

    Employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete=models.CASCADE, blank=True, null=True
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
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True)
    relationship = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.surname}"


class NextOfKinContract(models.Model):
    Employee = models.ForeignKey(
        EmployeeDetailsContract,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True)
    relationship = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

class MaleClothingPermanent(models.Model):

    Employee = models.ForeignKey(
        EmployeeDetailsPermanent,
        on_delete=models.CASCADE, blank=True, null=True
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
        on_delete=models.CASCADE, blank=True, null=True
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
