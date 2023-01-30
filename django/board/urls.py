from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('questions/', views.QuestionsView.as_view(), name='questions'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question'),
    path('answers/', views.AnswersView.as_view(), name='answers'),
    path('answers/<int:pk>/', views.AnswerDetailView.as_view(), name='answer'),
])
