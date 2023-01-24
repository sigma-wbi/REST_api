from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    #수정날짜 추가 blank=True: form.is_vaild()통한 데이터 검증 시 값이 없어도 된다

    def __str__(self):
        return self.subject  # 인스턴스가아닌 str로 출력


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Question 상속
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content
