from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(
        max_length=1,
        choices=[("M", "Male"), ("F", "Female")],
        blank=True,
        name="gender",
    )
    birthday = models.DateField(blank=True, null=True, name="birthday")
    phone = models.CharField(max_length=20, blank=True, name="phone")
