from django.shortcuts import render
from job_applications.models import Application

# Create your views here.
def home(request):
    return render(request, "users/home.html")

def register(request):
    return render(request, "users/register.html")