from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "common/signup.html", {"form": form})


from .forms import CheckPasswordForm
from django.contrib.auth.decorators import login_required

@login_required # 로그인하지 않은 사용자의 접근을 막기 위해 decorator를 추가
def delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete() # delete()로 DB에서 현재 user를 삭제하고 logout()을 통해 세션을 만료
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/common/login/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'common/delete.html', {'password_form':password_form})
