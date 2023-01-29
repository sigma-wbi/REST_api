from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from common.models import User
from board.models import Question,Answer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
import re
from dateutil.parser import parse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'gender/common': reverse('gender_common', request=request, format=format),
        'age/common': reverse('age_common', request=request, format=format),
        'gender/board': reverse('gender_board', request=request, format=format),
        'age/board/question': reverse('age_board_q', request=request, format=format),
        'age/board/answer': reverse('age_board_a', request=request, format=format),
        'usetime/common': reverse('use_time', request=request, format=format),
    })

class UserGenderStatisticView(APIView):
    """
    유저의 남녀 수를 확인합니다.
    """
    def get(self, request):
        male_cnt = User.objects.filter(gender="M").count()
        female_cnt = User.objects.filter(gender="F").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)

class UserAgeStatisticView(APIView):
    """
    유저의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        this_year=datetime.today().year
        for i in range(10):
            age_num = (
                User.objects
                .filter(birthday__range=[datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),12,31,23,59,59)])
                .distinct()
                .count()
            )
            if i == 0:
                age_key = '10대 미만 유저 수'
            else:
                age_key = str(i * 10) + '대 유저 수'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)


class BoardGenderStatisticView(APIView):
    """
    게시판에서 남녀의 분포를 확인합니다.
    """
    def get(self, request):
        male_Question_cnt = Question.objects.filter(author__gender="M").count()
        female_Question_cnt = Question.objects.filter(author__gender="F").count()
        male_Answer_cnt = Answer.objects.filter(author__gender="M").count()
        female_Answer_cnt = Answer.objects.filter(author__gender="F").count()
        return Response({"male_Question_count": male_Question_cnt, "female_Question_count": female_Question_cnt,"male_Answer_count": male_Answer_cnt, "female_Answer_count": female_Answer_cnt}, status=status.HTTP_200_OK)


class BoardAgeStatisticView_Q(APIView):
    """
    질문의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        this_year=datetime.today().year
        for i in range(10):
            age_num = (
                Question.objects.select_related("author")
                .filter(author__birthday__range=[datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),12,31,23,59,59)])
                .distinct()
                .values_list("author")
                .count()
            )
            if i == 0:
                age_key = '10대 미만 유저 질문 수'
            else:
                age_key = str(i * 10) + '대 유저 질문 수'

            result[age_key] = age_num
        
        return Response({"result": result}, status=status.HTTP_200_OK)
    
class BoardAgeStatisticView_A(APIView):
    """
    답변의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        this_year=datetime.today().year
        for i in range(10):
            age_num = (
                Answer.objects.select_related("author")
                .filter(author__birthday__range=[datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),12,31,23,59,59)])
                .distinct()
                .values_list("author")
                .count()
            )
            if i == 0:
                age_key = '10대 미만 유저 답변 수'
            else:
                age_key = str(i * 10) + '대 유저 답변 수'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)
    
class UserUsetimeStatisticView(APIView):
    """
    유저의 이용시간을 확인합니다.
    """
    def get(self, request):
        result = {}
        this_year=datetime.today().year
        for i in range(10):
            age_num = (
                User.objects
                .filter(date_joined__range=[datetime(this_year-((i+1))+1,1,1), datetime(this_year - (i),12,31,23,59,59)])
                .distinct()
                .count()
            )
            if i == 0:
                age_key = '1년 미만 유저 수'
            else:
                age_key = str(i) + '년차 유저 수'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)
    
    