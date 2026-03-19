from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserRegisterForm

# Create your views here.
def welcome(request):
    return render(request, 'users/welcome.html')

User = get_user_model()
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('home')

