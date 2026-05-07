from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserChangeEmailForm
from django.shortcuts import get_object_or_404

User = get_user_model()

def welcome_view(request):
    return render(request, 'users/welcome.html')

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/sign_up.html"
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = "users/login.html"
    next_page = reverse_lazy('home') # type: ignore

class UserChangeEmailView(SuccessMessageMixin, UpdateView):
    form_class = UserChangeEmailForm
    template_name = "users/change_email.html"

    success_message = "Email updated successfully!"
    success_url = reverse_lazy('home')

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)
    
class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "users/change_password.html"

    success_message = "Password updated successfully!"
    success_url = reverse_lazy('home')