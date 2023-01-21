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
        widgets = {
            'gender': forms.Select(attrs={'class':'form-control2'})
        }


from django.contrib.auth.hashers import check_password

class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}), 
    )
    # 현재 접속중인 사용자의 password를 가져오기
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
    # form에 입력된 password 값과 init으로 생성된 현재 사용자의 password 값을 django에서 제공하는 check_password를 통해 비교
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
