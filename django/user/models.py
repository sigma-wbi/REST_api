from django.db import models

# from django.contrib.auth.models import User
from django.conf import settings

# from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject  # 인스턴스가아닌 str로 출력


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Question 상속
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content
