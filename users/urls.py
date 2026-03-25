from django.urls import path
from .views import RegisterView, welcome_view, UserLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('/register', RegisterView.as_view(), name='register'),
    path('/login', UserLoginView.as_view(), name='login'),
    path('/logout', LogoutView.as_view(next_page='home'), name='logout')
]