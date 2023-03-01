from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Allergen(models.Model):
    name = models.CharField(max_length=100)
    allergens = models.TextField()

    def __str__(self) -> str:
        return self.name

class Patient(models.Model):
    GENDER = [ 
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    
    @property
    def patient_id(self):
        return "p_" + str(self.id)

    surname = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=100, choices=GENDER)
    birthday = models.DateField()

    address = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null = True, blank= True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    ##### CHANGE CASCADE WHEN WORKING!!!
    user = models.OneToOneField(User, null=True, blank= True, on_delete=models.CASCADE, related_name='patient')
    
    def __str__(self) -> str:
        return self.patient_id

class Staff(models.Model):
    GENDER = [ 
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    POSITION = [
        ('NURSE','NURSE'),
        ('DOCTOR', 'DOCTOR'),
        ('RECEPTIONIST', 'RECEPTIONIST'),
    ]

    DEPARTMENT = [
        ('Emergency', 'Emergency'),
        ('Intensive Care', 'Intensive Care'),
        ('Surgery', 'Surgery'),
        ('Radiology', 'Radiology'),
        ('Laboratory', 'Laboratory'),
        ('Physical Therapy', 'Physical Therapy'),
        ('Pharmacy', 'Pharmacy'),
        ('Mental Health', 'Mental Health'),
        ('Oncology', 'Oncology'),
        ('Orthopedics', 'Orthopedics'),
        ('Neurology', 'Neurology'),
        ('Cardiology', 'Cardiology'),
        ('Endocrinology', 'Endocrinology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Dermatology', 'Dermatology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Rheumatology', 'Rheumatology'),
        ('Pulmonology', 'Pulmonology'),
        ('Infectious Diseases', 'Infectious Diseases'),
        ('Nephrology', 'Nephrology'),
        ('General', 'General'),
    ]

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    birthday = models.DateField()

    address = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null = True, blank= True)
    date_created = models.DateTimeField()

    position = models.CharField(max_length=100, choices=POSITION)
    department = models.CharField(max_length=100, choices=DEPARTMENT)

    user_name = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='staffUsername')

    @property
    def staff_id(self):
        if self.position == 'NURSE':
            return "n_" + str(self.id)
        elif self.position == 'DOCTOR':
            return "d_" + str(self.id)
        elif self.position == 'RECEPTIONIST':
            return "r_" + str(self.id)

    def __str__(self) -> str:
        return self.staff_id


class Diagnosis(models.Model):
    diagnosis_id = models.CharField(max_length=10)
    short_desciption = models.CharField(max_length= 100)
    long_desciption = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.short_desciption


class PatientHasAllergy(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, name='pid')
    allergy = models.ManyToManyField(Allergen)

    def __str__(self) -> str:
        return self.patient.name


class Condition_Check_UP(models.Model):

    MENTAL_STATE = [
        ('Stable','Stable'),
        ('Mildly distressed','Mildly distressed'),
        ('Moderately distressed','Moderately distressed'),
        ('Severely distressed','Severely distressed'),
        ('Acutely psychotic','Acutely psychotic'),
    ]

    YES_NO = [
        ('Yes', 'Yes'),
        ('Sometimes','Sometimes'),
        ('No', 'No'),
    ]

    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, related_name = 'checkuppid')
    nurse = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL, related_name = 'nurse')

    heigth = models.CharField(max_length=5)
    weigth = models.CharField(max_length=5)

    urgency = models.CharField(max_length=15, choices=YES_NO)
    abnormal_breathing = models.CharField(max_length=15, choices=YES_NO)
    smokes = models.CharField(max_length=15, choices=YES_NO)
    drinks = models.CharField(max_length=15, choices=YES_NO)
    has_headache = models.CharField(max_length=15, choices=YES_NO)
    mental_state = models.CharField(max_length=50, choices=MENTAL_STATE)

    heart_rate = models.CharField(max_length=20)
    blood_presure = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)

    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        show_up = str(str(self.date) + " -- " + self.patient.name )
        return show_up


class PatientHasDiagnosis(models.Model):
    patient_id = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, related_name='patient')
    doctor = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    diagnosis = models.ForeignKey(Diagnosis, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    treatment = models.CharField(max_length=500)


class NextAppointment(models.Model):
    patient = models.ForeignKey(Patient,null=True, on_delete=models.SET_NULL, related_name='patient_next_app')
    staff = models.ForeignKey(Staff,null=True, on_delete=models.SET_NULL, related_name = 'staff')
    receptionits = models.ForeignKey(Staff,null=True, on_delete=models.SET_NULL, related_name='receptionist')
    date = models.DateTimeField()

    def __str__(self) -> str:
        show_up = str(self.patient.name + " -- " + str(self.date) + " -- " + self.staff.name)
        return show_up
    