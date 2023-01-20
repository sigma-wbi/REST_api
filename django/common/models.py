from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser 불러오기
from django.conf import settings


class User(AbstractUser):  # 왜 상속이 안되지?
    test = models.CharField(max_length=30, default="sss")
