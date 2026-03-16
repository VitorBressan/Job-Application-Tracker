from django.contrib import admin
from .models import Application, ApplicationEvent


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass

@admin.register(ApplicationEvent)
class ApplcationEventAdmin(admin.ModelAdmin):
    pass

