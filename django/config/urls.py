from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/common/', include('common.urls')),
    path('api/board/', include('board.urls')),
    path('api/statistic/', include('statistic.urls')),
    path('api/log/', include('log.urls')),
]
