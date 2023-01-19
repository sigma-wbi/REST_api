from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    sex_choices =[
        ('선택', None),
        ('남', '남자'),
        ('여', '여자'),
    ]
    email = forms.EmailField(label="이메일")
    sex = forms.ChoiceField(choices=sex_choices, required=True) # required=True 속성에 위배될시 에러가 나며 폼 제출 및 저장이 수행되지않는다.
    birth = forms.DateField(label='생년월일')
    

    class Meta:
        model = User
        fields = ("username", "sex", "birth","password1", "password2", "email", "last_login")