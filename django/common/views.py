from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import User

# User = get_user_model()
# User = settings.AUTH_USER_MODEL


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # 어찌하여....
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "common/signup.html", {"form": form})
