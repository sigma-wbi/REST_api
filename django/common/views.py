from django.contrib.auth import get_user_model
from .serializers import UserSerializer, SignupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users', request=request, format=format),
        'signup': reverse('signup', request=request, format=format),
        'token': reverse('token_obtain_pair', request=request, format=format),
        'token/refresh': reverse('token_refresh', request=request, format=format),
        'token/verify': reverse('token_verify', request=request, format=format),
        # 'withdraw': reverse('withdraw', request=request, format=format),
    })


class UsersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all().order_by('-date_joined')    
    serializer_class = UserSerializer


class SignupView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SignupSerializer
        
     
class WithdrawView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
