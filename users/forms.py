from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    
    class Meta:
        model = get_user_model()
        #fields = UserCreationForm.Meta.fields + ("email", )
        