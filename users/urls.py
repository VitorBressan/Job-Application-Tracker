from django.urls import path
from .views import UserRegisterView, welcome_view, UserLoginView, UserChangeEmailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('sign-up', UserRegisterView.as_view(), name='sign-up'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='welcome'), name='logout'),
    path('change-email', UserChangeEmailView.as_view(), name='change_email'),
    path('change-email', UserChangeEmailView.as_view(), name='change_password'),
]