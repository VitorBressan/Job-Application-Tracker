from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('application/add/', AddApplicationView.as_view(), name='add_application'),
    path('application/<int:application_id>/', application_details, name='application'),
    path('application/<int:application_id>/event/add/', add_event, name='add_event'),
    path('application/<int:application_id>/delete/', delete_application, name='delete_application'),
    path('application/<int:application_id>/event/<int:event_id>/delete/', delete_application_event, name="delete_event")
]
