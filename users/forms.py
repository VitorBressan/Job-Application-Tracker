from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML, Div
from django.urls import reverse

User = get_user_model()
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class UserChangeEmailForm(ModelForm):
    class Meta:
        model = User
        fields = ("email", )
        labels = {
            'email': 'New Email Address',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        
        self.helper.form_action = reverse("change_email")
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            
            Row(
                Column('email', css_class='form-group col-12 mb-3'),
            ),
            
            
            HTML('<p class="text-muted small mb-4">Note: You will use this new email the next time you log in.</p>'),

            # Buttons
            Div(
                # Cancel Button
                HTML(f"""
                    <a href="{reverse('home')}" 
                       class="btn btn-outline-secondary px-4 rounded-pill">
                       Cancel
                    </a>
                """),
                # Submit Button
                Submit('submit', 'Update Email', css_class='btn btn-primary px-4 rounded-pill shadow-sm'),

                css_class="d-flex justify-content-between mt-2"
            )
        )
        
        # Placeholder
        self.fields['email'].widget.attrs.update({'placeholder': 'example@email.com'})

    
