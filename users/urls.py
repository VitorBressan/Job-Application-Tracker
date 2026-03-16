from django.urls import path
from .views import home, register

urlpatterns = [
    path("", register, name="register")
]