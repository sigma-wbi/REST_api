from django.urls import path

from . import views

app_name = 'user' # name space지정해주면 하드코딩으로부터 벗어날 수 있다. 
urlpatterns = [
    path('', views.index, name='index'), # 기존 ayaan에서 user로 매핑되었기때문에 홈디렉토리가됨
    path('<int:question_id>/', views.detail, name='detail'), #/ 빼먹지말자
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
