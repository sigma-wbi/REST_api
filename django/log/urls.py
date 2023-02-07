from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('logs/', views.LogsView.as_view(), name='logs'),
])
