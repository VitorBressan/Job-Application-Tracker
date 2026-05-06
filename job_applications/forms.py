from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML, Div
from django.urls import reverse
from .models import *

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = [
            'company_name', 'role', 'vacancy_link', 'status', 
            'vacancy_description', 'work_mode', 'contract_type', 
            'company_address', 'date_applied', 'notes', 
            'salary_min', 'salary_max', 'salary_period', 'currency'
        ]

    def __init__(self, *args, **kwargs):

        app_id = kwargs.pop('application_id', None)
        next_url = kwargs.pop('next', None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        if app_id:
            action_url = reverse('edit_application', args=[app_id])
        else:
            action_url = reverse('add_application')
        if next_url:
                action_url += f"?next={next_url}"

        self.helper.form_action = action_url
        
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            # Main Details
            Row(
                Column('company_name', css_class='form-group col-md-6 mb-3'),
                Column('role', css_class='form-group col-md-6 mb-3'),
            ),
            
            Row(
                Column('vacancy_link', css_class='form-group col-md-8 mb-3'),
                Column('status', css_class='form-group col-md-4 mb-3'),
            ),

            Row(
                Column('work_mode', css_class='form-group col-md-4 mb-3'),
                Column('contract_type', css_class='form-group col-md-4 mb-3'),
                Column('date_applied', css_class='form-group col-md-4 mb-3'),
            ),

            'company_address',

            # Text Areas
            'vacancy_description',
            'notes',

            # Salary
            HTML('<h6 class="fw-bold mt-3 mb-2">Salary Information</h6>'),
            Row(
                Column('salary_min', css_class='form-group col-md-3 mb-3'),
                Column('salary_max', css_class='form-group col-md-3 mb-3'),
                Column('currency', css_class='form-group col-md-3 mb-3'),
                Column('salary_period', css_class='form-group col-md-3 mb-3'),
            ),

            # Buttons
            Div(
                # The Cancel Button
                HTML(f"""
                    <a href="{next_url or reverse('home')}" 
                       class="btn btn-outline-secondary px-4 rounded-pill">
                       Cancel
                    </a>
                """),
                # The Submit Button
                Submit('submit', 'Save Application', css_class='btn btn-primary px-4 rounded-pill'),

                css_class="d-flex justify-content-end gap-2" 
            )
        )
        
        self.fields['vacancy_description'].widget.attrs.update({'rows': '4'})
        self.fields['notes'].widget.attrs.update({'rows': '3'})

        self.fields['salary_min'].widget.attrs.update({'placeholder': 'e.g. 5000 (Optional)'})
        self.fields['salary_max'].widget.attrs.update({'placeholder': 'e.g. 7000 (Optional)'})
        self.fields['vacancy_description'].widget.attrs.update({
            'placeholder': 'Copy and paste the vacancy description here...'
        })

        # "Optional" on every field that isn't required automatically:
        for field_name, field in self.fields.items():
            if not field.required and 'placeholder' not in field.widget.attrs:
                field.widget.attrs['placeholder'] = 'Optional'


class EventForm(ModelForm):
    class Meta:
        model = ApplicationEvent
        fields = ["event_type", "notes", "event_date"]
        widgets = {
            'event_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
        