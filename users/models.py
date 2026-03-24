from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    # Custom email field ( Made it required and unique )
    email = models.EmailField(verbose_name="Email", unique=True, blank=False, null=False)

    # Custom username field ( Made it not unique )
    username = models.CharField(verbose_name="Username", max_length=100, blank=False, null=False)

    # Make email as the user identifier ( Django default is "username")
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email