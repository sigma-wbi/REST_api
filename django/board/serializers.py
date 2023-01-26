from .models import Question, Answer
from rest_framework import serializers


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['author', 'create_date', 'modify_date']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['author', 'create_date', 'modify_date']