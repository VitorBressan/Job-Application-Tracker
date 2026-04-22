from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from .models import *
from django.urls import reverse_lazy, reverse
from .forms import *


@login_required
def home(request):
    search_query = request.GET.get('search')
    if search_query:
        applications = Application.objects.filter(
            company_name__icontains=search_query,
            user = request.user
        )
    else:
        applications = Application.objects.filter(user = request.user)

    status = request.GET.get('status')
    if status:
        applications = applications.filter(status=status)

    sort_by = request.GET.get('sort')
    if sort_by:
        applications = applications.order_by('date_applied' if sort_by == 'oldest' else '-date_applied')

    data = {
        "applications_list": applications,
    }
    return render(request, "job_applications/home.html", context=data)

class AddApplicationView(CreateView):
    form_class = ApplicationForm
    template_name = 'job_applications/add_application.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        application_object = form.save(commit=False)
        application_object.user = self.request.user
        application_object.save()
        return super().form_valid(form)
    
def delete_application(request, application_id: int):
    if request.method == "POST":
        get_object_or_404(Application, id=application_id).delete()
    return redirect('home')

class EditApplicationView(UpdateView):
    form_class = ApplicationForm
    template_name = 'job_applications/edit_application.html'

    def get_success_url(self):
        next_url= self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse('home')

    def get_object(self):
        return get_object_or_404(Application, pk=self.kwargs.get('application_id'))
    

def application_details(request, application_id: int):
    application = get_object_or_404(Application, id=application_id)
    event_form = EventForm()
    events = ApplicationEvent.objects.filter(application_id = application.pk).order_by("-event_date", "-id")
    
    data = {
        "application": application,
        "form": event_form,
        "events": events,
    }
    return render(request, "job_applications/application.html", context=data)

def add_application_event(request, application_id: int):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False) 
            event.application = get_object_or_404(Application, id=application_id)
            event.save()
    return redirect('application', application_id=application_id)

def edit_application_event(request, application_id: int, event_id: int):
    event = get_object_or_404(ApplicationEvent, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form = form.save()
    return redirect('application', application_id=application_id)

def delete_application_event(request, application_id: int, event_id: int):
    if request.method == "POST":
        get_object_or_404(ApplicationEvent, id=event_id).delete()
    return redirect('application', application_id=application_id)

