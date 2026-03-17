from django.urls import path
from .views import RegisterView, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('/register', RegisterView.as_view(), name='register')
]