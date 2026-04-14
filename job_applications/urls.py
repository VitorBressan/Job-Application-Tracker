from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add-application', AddApplicationView.as_view(), name='add_application'),
    path('application/<int:application_id>/', application_details, name='application'),
    path('application/<int:application_id>/add-event', add_event, name='add_event'),
    path('application/delete/<int:application_id>', delete_application, name='delete_application')
]