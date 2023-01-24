from django.contrib import admin
from django.urls import path, include
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('board/', include('board.urls')), # user 앱의 views.index호출 / include를 사용해 url분리
    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('api/', include('api.urls')),
]
