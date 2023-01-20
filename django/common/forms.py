from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User  # 유저모델 상속

from django.contrib.auth import get_user_model

# User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        models = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]
