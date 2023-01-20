from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User  # 유저모델 상속

from django.contrib.auth import get_user_model
from django.conf import settings

# User = get_user_model()
# User = settings.AUTH_USER_MODEL


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  #  get_user_model() 해야되는 이유 찾기
        fields = UserCreationForm.Meta.fields + ("gender", "birthday", "phone")
