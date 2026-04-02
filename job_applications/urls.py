from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add-application', AddApplicationView.as_view(), name='add_application'),
    path('application/<int:id>/', application_details, name='application'),
]