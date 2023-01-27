from .models import Question, Answer
from .serializers import QuestionsSerializer, AnswersSerializer
from .permissions import IsAuthorOrReadOnly
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


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


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

    def perform_update(self, serializer):
        serializer.save(modify_date=timezone.now())


class AnswersView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all().order_by('-create_date')    
    serializer_class = AnswersSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

    def perform_update(self, serializer):
        serializer.save(modify_date=timezone.now())