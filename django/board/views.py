from .models import Question, Answer
from .serializers import QuestionsSerializer, AnswersSerializer
from .permissions import IsAuthorOrReadOnly
from django.utils import timezone
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
        'questions': reverse('questions', request=request, format=format),
        'answers': reverse('answers', request=request, format=format),
    })


class QuestionsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all().order_by('-create_date')    
    serializer_class = QuestionsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        logger.info('Question List', extra={'request': self.request})
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        logger.info('Question Create', extra={'request': self.request})
        return super().create(request, *args, **kwargs)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

    def perform_update(self, serializer):
        serializer.save(modify_date=timezone.now())

    def retrieve(self, request, *args, **kwargs):
        logger.info('Question Retrieve', extra={'request': self.request})
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        logger.info('Question Update', extra={'request': self.request})
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        logger.info('Question Destroy', extra={'request': self.request})
        return super().destroy(request, *args, **kwargs)


class AnswersView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all().order_by('-create_date')    
    serializer_class = AnswersSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        logger.info('Answer List', extra={'request': self.request})
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        logger.info('Answer Create', extra={'request': self.request})
        return super().create(request, *args, **kwargs)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

    def perform_update(self, serializer):
        serializer.save(modify_date=timezone.now())

    def retrieve(self, request, *args, **kwargs):
        logger.info('Answer Retrieve', extra={'request': self.request})
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        logger.info('Answer Update', extra={'request': self.request})
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        logger.info('Answer Destroy', extra={'request': self.request})
        return super().destroy(request, *args, **kwargs)