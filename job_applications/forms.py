from django.forms import ModelForm, DateInput
from .models import *

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['company_name', 'role', 'vacancy_link', 'status', 'vacancy_description','work_mode', 'contract_type', 'company_address', 'date_applied', 'notes', 'salary_min', 'salary_max', 'salary_period', 'currency', ]
        help_texts = {
            'company_address': 'Optional',
            'notes': 'Optional',
            'salary_min': 'Fill min and max salary with the same amount if the salary is fix (Optional)',
            'salary_max': 'Fill min and max salary with the same amount if the salary is fix (Optional)',
            'salary_period': 'Optional',
            'currency': 'Optional',
            'work_mode': 'Optional',
            'contract_type': 'Optional',
            'vacancy_description': 'Copy and paste de vacancy description here (Optional)'
        }

class EventForm(ModelForm):
    class Meta:
        model = ApplicationEvent
        fields = ["event_type", "notes", "event_date"]
        widgets = {
            'event_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
        