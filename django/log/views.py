from .serializers import LogSerializer
from .models import Log
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

import logging
logger = logging.getLogger('my_json')

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'logs': reverse('logs', request=request, format=format),
    })


class LogsView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Log.objects.all().order_by('-time')
    serializer_class = LogSerializer
