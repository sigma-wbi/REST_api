from django.contrib import admin
from .models import Question, Answer
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject','content'] #검색필드 커스텀
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)