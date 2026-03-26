from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import *
from .forms import ApplicationRegisterForm  

@login_required
def home(request):
    return render(request, "job_applications/home.html")

class AddApplicationView(CreateView):
    form_class = ApplicationRegisterForm
    template_name = 'job_applications/add_application.html'