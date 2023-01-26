from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UsersView.as_view(), name='users'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('withdraw/<int:pk>/', views.WithdrawView.as_view(), name='withdraw'),
])
