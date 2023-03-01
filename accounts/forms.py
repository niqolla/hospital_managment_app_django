from django import forms
from django.forms import DateInput
from django.forms import DateTimeInput
# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import *

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
        }

class DiagnosisForm(forms.ModelForm):    
    class Meta:
        model = PatientHasDiagnosis
        fields = '__all__'

class CheckUpForm(forms.ModelForm):
    class Meta:
        model = Condition_Check_UP
        fields = '__all__'

class AllergensForm(forms.ModelForm):
    class Meta:
        model = PatientHasAllergy
        fields = '__all__'
        widgets = {
            'allergy': forms.CheckboxSelectMultiple
        }

class NewAppointment(forms.ModelForm):
    class Meta:
        model = NextAppointment
        fields = ['patient', 'staff', 'receptionits', 'date']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']