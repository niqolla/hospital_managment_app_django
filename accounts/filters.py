import django_filters 
from django_filters import DateFilter
from .models import *

class DiagFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name ='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')
    class Meta:
        model = PatientHasDiagnosis
        fields = ['date', 'diagnosis', 'start_date', 'end_date']

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        # fields = '__all__'
        fields = ['id','name', 'surname']