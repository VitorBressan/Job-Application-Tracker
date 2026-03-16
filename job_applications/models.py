from django.db import models
from django.conf import settings

# Create your models here.
CONTRACT_TYPE_CHOICES = [
    ("PJ", "PJ"),
    ("CLT", "CLT"),
    ("FREELANCE", "Freelance")
]
STATUS_CHOICES = [
    ("APPLIED", "Applied"),
    ("GHOSTED", "Ghosted"),
    ("REJECTED", "Rejected"),
    ("IN PROCESS", "In Process"),
    ("OFFERED", "Offered"),
    ("ACCEPTED", "Accepted")
]
WORK_MODE_CHOICES = [
    ("REMOTE", "Remote"),
    ("HYBRID", "Hybrid"),
    ("ON-SITE", "On-Site")
]
CURRENCY_CHOICES = [
    ("BRL", "BRL"),
    ("USD", "USD"),
    ("EUR", "EUR")
]
SALARY_PERIOD_CHOICES = [
    ("MONTHLY", "Monthly"),
    ("YEARLY", "Yearly"),
    ("HOURLY", "Hourly")
]
class Application(models.Model):
    company_name = models.CharField(verbose_name="Company Name", max_length=100)
    role = models.CharField(verbose_name="Role", max_length=100)
    vacancy_link = models.URLField(verbose_name="Vacancy Link")
    vacancy_description = models.TextField(verbose_name="Vacancy Description")
    company_address = models.CharField(verbose_name="Company Address", null=True, blank=True)
    contract_type = models.CharField(
        verbose_name="Contract Type",
        max_length=20,
        choices=CONTRACT_TYPE_CHOICES,
        null=True, blank=True
    )
    status = models.CharField(verbose_name="Status", max_length=20, choices=STATUS_CHOICES, default="APPLIED")
    date_applied = models.DateField(verbose_name="Date Applied")
    notes = models.TextField(verbose_name="Notes", null=True, blank=True)
    salary_min = models.IntegerField(verbose_name="Minimum Salary", null=True, blank=True)
    salary_max = models.IntegerField(verbose_name="Maximum Salary", null=True, blank=True)
    salary_period = models.CharField(verbose_name="Salary Period", max_length=10, choices=SALARY_PERIOD_CHOICES, null=True, blank=True)
    currency = models.CharField(verbose_name="Currency", max_length=5, choices=CURRENCY_CHOICES, null=True, blank=True)
    work_mode = models.CharField (verbose_name="Work Mode", max_length=10, choices=WORK_MODE_CHOICES, null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

EVENT_TYPE_CHOICES = [
    ("RECRUITER CONTACT", "Recruiter Contact"),
    ("INTERVIEW", "Interview"),
    ("TECHNICAL INTERVIEW", "Technical Interview"),
    ("REJECTED", "Rejected"),
    ("ACCEPTED", "Accepted")
]
class ApplicationEvent(models.Model):
    event_type = models.CharField(verbose_name="Event Type", max_length=30, choices=EVENT_TYPE_CHOICES)
    notes = models.TextField(verbose_name="Notes", null=True, blank=True)
    event_date = models.DateField("Event Date")

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="events")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)