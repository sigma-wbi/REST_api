from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser 불러오기
from django.conf import settings


class User(AbstractUser):  # 왜 상속이 안되지?

    # sex = models.Choices(max_length=30,cho blank=False)
    # phone = models.CharField(max_length=30, default="sss", blank=False)
    # birth = models.DateField(null=True, blank=False) # 확인
    gender = models.CharField(
        max_length=1,
        choices=[("M", "Male"), ("F", "Female")],
        blank=True,
        name="gender",
    )
    birthday = models.DateField(blank=True, null=True, name="birthday")
    phone = models.CharField(max_length=11, blank=True, name="phone")
