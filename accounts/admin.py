from django.contrib import admin
from .models import *

# Register your models here.



# admin.site.register(Patient)
# admin.site.register(Staff)
admin.site.register(PatientHasAllergy)
admin.site.register(Allergen)
admin.site.register(Diagnosis)
admin.site.register(Condition_Check_UP)
admin.site.register(PatientHasDiagnosis)
admin.site.register(NextAppointment)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'name', 'surname', 'gender')


@admin.register(Staff)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'name', 'surname', 'position', 'department')


