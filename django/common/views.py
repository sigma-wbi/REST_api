from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, SignupSerializer
from .permissions import IsUserOrStaff
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

import logging
logger = logging.getLogger('my_json')

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users', request=request, format=format),
        'signup': reverse('signup', request=request, format=format),
        'token': reverse('token_obtain_pair', request=request, format=format),
        'token/refresh': reverse('token_refresh', request=request, format=format),
        'token/verify': reverse('token_verify', request=request, format=format),
    })


class UsersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all().order_by('-date_joined')    
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        logger.info('User List', extra={'request': self.request})
        return super().list(request, *args, **kwargs)


class SignupView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        logger.info('User Create', extra={'request': self.request})
        return super().create(request, *args, **kwargs)
        
        
class WithdrawView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsUserOrStaff]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        logger.info('User Destroy', extra={'request': self.request})
        return super().destroy(request, *args, **kwargs)
