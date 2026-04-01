from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import *
from django.urls import reverse_lazy
from .forms import ApplicationRegisterForm  

@login_required
def home(request):
    applications = Application.objects.filter(user = request.user)
    data = {
        "applications_list": applications
    }
    return render(request, "job_applications/home.html", context=data)

class AddApplicationView(CreateView):
    form_class = ApplicationRegisterForm
    template_name = 'job_applications/add_application.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        application_object = form.save(commit=False)
        application_object.user = self.request.user
        application_object.save()
        return super().form_valid(form)