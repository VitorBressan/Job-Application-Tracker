from django.urls import path
from .views import RegisterView, welcome_view, UserLoginView

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('/register', RegisterView.as_view(), name='register'),
    path('/login', UserLoginView.as_view(),name='login')
]