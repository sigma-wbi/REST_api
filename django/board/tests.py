from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

from common.models import User
from .models import Answer,Question


class Testboard(APITestCase):

    # 더미데이터 생성 함수명 setUp 지켜야함
    def setUp(self):
        self.question_url = "/api/board/questions/"
        self.user = User.objects.create(
            id       = 1,
            username = "testboard",
            password = make_password("kkkk1234"),
            email    = "aaaaa@naver.com",
            gender   = "M",
            birthday = "2023-01-25",
            phone    = "010-1111-1111"
            )
        # 타 유저가 게시물 수정가능함
        self.user1 = User.objects.create(
            id       = 2,
            username = "testboard2",
            password = make_password("kkkk1234"),
            email    = "bbbbb@naver.com",
            gender   = "F",
            birthday = "2023-01-25",
            phone    = "010-2222-2222"
            )    
        self.question = Question.objects.create(
            id        = 1,
            author    = self.user, # User의 instance로 받아야함
            subject   = "제목 1",
            content   = "내용 1"
        )
        self.question_url2 = f"/api/board/questions/"
    
    # def tearDown(self): # 임시 데이터 삭제 O / X
    #     User.objects.all().delete()
    #     Question.objects.all().delete()

    def test_board_lists_login(self):  # 로그인시 게시판 조회
        self.refresh = RefreshToken.for_user(self.user) # 토큰 refresh, access token 해킹방지용
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        # client = APIClient()
        # client.force_authenticate(user=self.user)
        
        self.response = self.client.get(self.question_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK, msg="게시판 조회 실패")


    def test_board_lists(self): # 비 로그인시 게시판 조회

        self.response = self.client.get(self.question_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="비로그인시 게시판 조회되면 안됨") #미인증 시 403출력

    
    def test_board_detail_login(self):  # 로그인시 상세페이지 조회
        self.refresh = RefreshToken.for_user(self.user) # 토큰 refresh, access token 해킹방지용
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.get(f'{self.question_url2}{self.question.id}/', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK, msg="상세 페이지 조회 실패")

    
    def test_board_detail(self): # 비 로그인시 상세페이지 조회

        self.response = self.client.get(f'{self.question_url2}{self.question.id}/', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="비로그인시 상세페이지 조회되면 안됨")


    def test_board_create_login(self): # 로그인시 글작성
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "subject"  : "DE-webframework",
            "content": "It's getting harder...."
        }

        self.response = self.client.post(self.question_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED, msg="글 작성 실패")
    
    def test_board_create(self): # 비 로그인시 글작성

        data = {
            "subject"  : "DE-webframework",
            "content": "It's getting harder...."
        }

        self.response = self.client.post(self.question_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="비로그인시 게시판 작성되면 안됨")


# --------------put, delete는 상세페이지---------------------

    def test_detail_board_update_login(self): # 로그인시 상세페이지에서 수정
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')

        data = {
            "subject"  : "DRF",
            "content": "It's getting harder, but I think I know...."
        }
        self.response = self.client.put(f'{self.question_url2}{self.question.id}/', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK, msg="상세페이지 수정 안됨")


    def test_detail_board_update(self): # 비 로그인시 상세페이지에서 수정
        data = {
            "subject"  : "DRF",
            "content": "It's getting harder, but I think I know...."
        }
        self.response = self.client.put(f'{self.question_url2}{self.question.id}/', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="비로그인시 상세페이지 수정되면 안됨")
       

    def test_detail_board_update_noself(self): # 타인 로그인 상세페이지에서 수정
        self.refresh = RefreshToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        data = {
            "subject"  : "DRF!!!",
            "content": "It's getting harder, I don't know...."
        }

        self.response = self.client.put(f'{self.question_url2}{self.question.id}/', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="타인 로그인시 상세페이지 수정되면 안됨")


    def test_detail_board_delete_login(self): # 로그인시 상세페이지에서 삭제
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')

        self.response = self.client.delete(f'{self.question_url2}{self.question.id}/', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT, msg="상세페이지 삭제 안됨")


    def test_detail_board_delete(self):# 비 로그인시 상세페이지에서 삭제

        self.response = self.client.delete(f'{self.question_url2}{self.question.id}/', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="비로그인시 상세페이지 삭제되면 안됨")


    def test_detail_board_delete_noself(self): # 타인 로그인 상세페이지에서 삭제
        self.refresh = RefreshToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')

        self.response = self.client.delete(f'{self.question_url2}{self.question.id}/', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="타인 로그인시 상세페이지 삭제되면 안됨")