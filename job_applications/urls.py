from django.urls import path
from .views import home, AddApplicationView

urlpatterns = [
    path('', home, name='home'),
    path('add-application', AddApplicationView.as_view(), name='add_application')
]