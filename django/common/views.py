from django.contrib.auth import get_user_model
from .serializers import UserSerializer, SignupSerializer
from rest_framework import generics, viewsets


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class SignupView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SignupSerializer