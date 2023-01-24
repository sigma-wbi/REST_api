from django.urls import path

from . import views

app_name = 'board' # name space지정해주면 하드코딩으로부터 벗어날 수 있다. 
urlpatterns = [
    path('', views.index, name='index'), # 기존 config에서 board로 매핑되었기때문에 홈디렉토리가됨
    path('<int:question_id>/', views.detail, name='detail'), 
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
