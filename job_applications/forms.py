from django.forms import ModelForm
from .models import Application

class ApplicationRegisterForm(ModelForm):
    class Meta:
        model = Application
        fields = ['company_name', 'role', 'vacancy_link', 'company_address','status', 'date_applied', 'notes', 'salary_min', 'salary_max', 'salary_period', 'currency', 'work_mode']
        help_texts = {
            'company_adress': 'Optional',
            'notes': 'Optional',
            'salary_min': 'Fill min and max salary with the same amount if the salary is fix (Optional)',
            'salary_max': 'Fill min and max salary with the same amount if the salary is fix (Optional)',
            'salary_period': 'Optional',
            'currency': 'Optional',
            'work_mode': 'Optional'
        }
