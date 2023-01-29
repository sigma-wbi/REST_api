from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gender/common', views.UserGenderStatisticView.as_view(), name='gender_common'),
    path('age/common', views.UserAgeStatisticView.as_view(), name='age_common'),
    path('gender/board', views.BoardGenderStatisticView.as_view(), name='gender_board'),
    path('age/board/question', views.BoardAgeStatisticView_Q.as_view(), name='age_board_q'),
    path('age/board/answer', views.BoardAgeStatisticView_A.as_view(), name='age_board_a'),
    path('usetime/common', views.UserUsetimeStatisticView.as_view(), name='use_time'),
])