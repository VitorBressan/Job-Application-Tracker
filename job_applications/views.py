from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import *
from django.urls import reverse_lazy
from .forms import *

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
    
def application_details(request, application_id: int):
    application = get_object_or_404(Application, id=application_id)
    event_form = AddEventForm()
    events = ApplicationEvent.objects.filter(application_id = application.pk).order_by("-event_date", "-id")
    
    data = {
        "application": application,
        "form": event_form,
        "events": events,
    }
    return render(request, "job_applications/application.html", context=data)

def add_event(request, application_id: int):
    application = get_object_or_404(Application, id=application_id)
    if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.application = application
            event.save()
    return redirect('application', application_id=application.pk)
