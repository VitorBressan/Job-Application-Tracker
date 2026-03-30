from django.contrib import admin
from .models import Application, ApplicationEvent


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("company_name", "role", "created_at")
    readonly_fields = ("created_at",)

@admin.register(ApplicationEvent)
class ApplcationEventAdmin(admin.ModelAdmin):
    pass

