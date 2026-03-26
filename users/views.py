from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserRegisterForm

# Create your views here.
def welcome_view(request):
    return render(request, 'users/welcome.html')

User = get_user_model()
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/sign_up.html"
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = "users/login.html"
    next_page = reverse_lazy('home')

class LogoutView(): 
    pass