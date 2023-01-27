from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password # 해싱된 암호 생성
from rest_framework import status
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class Testuser(APITestCase):
    
    def setUp(self): # 더미데이터 생성 함수명 setUp 지켜야함
        self.user = User.objects.create(
            id       = 1,
            username = "testuser",
            password = make_password("kkkk1234"),
            email    = "aaaaa@naver.com",
            gender   = "M",
            birthday = "2023-01-25",
            phone    = "010-1111-1111"
            )
        # 타 유저가 게시물 수정가능함
        self.user1 = User.objects.create(
            id       = 2,
            username = "testuser2",
            password = make_password("kkkk1234"),
            email    = "bbbbb@naver.com",
            gender   = "F",
            birthday = "2023-01-25",
            phone    = "010-2222-2222"
            )   
        self.url = "/api/common/signup/"
        self.withdraw_url = f"/api/common/withdraw/{self.user.id}/" # 마지막에 /주의 301 error
        self.token_url = "/api/common/token/"
        self.token_refresh_url = "/api/common/token/refresh/"
        self.token_verify_ulr = "/api/common/token/verify/"
        self.user.save()
        self.assertIsNotNone(self.user, msg="유저가 생성되지 않았습니다.")

    def test_signup(self): #회원가입
        self.user_info = {
            "username" : 'testuser1',
            "password1" : "kkkk1234",
            "password2" : "kkkk1234",
            "email" : "ayaan@naver.com",
            "gender" : "M",
            "birthday" : "2023-01-26",
            "phone" : "010-1111-1111"
        }
        self.response = self.client.post(self.url, data = self.user_info, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED, msg="회원가입테스트가 정상 진행 되지 않았습니다.") # 같은지 확인

    def test_signup_dupli_id_check(self): #중복아이디 체크
        self.user_info = {
            "username" : 'testuser', # 처음 생성된 아이디와 중복
            "password1" : "kkkk1234",
            "password2" : "kkkk1234",
            "email" : "ayaan@naver.com",
            "gender" : "M",
            "birthday" : "2023-01-26",
            "phone" : "010-1111-1111"
        }
        self.response = self.client.post(self.url, data = self.user_info, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST, msg="중복체크가 제대로 되지않습니다.")

    def test_signup_password_check(self): #비밀번호 불일치

        self.user_info = {
            "username" : 'testuser1', 
            "password1" : "kkkk1234",
            "password2" : "aaaa1234", # 비밀번호 다름
            "email" : "ayaan@naver.com",
            "gender" : "M",
            "birthday" : "2023-01-26",
            "phone" : "010-1111-1111"
        }
        self.response = self.client.post(self.url, data = self.user_info, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST, msg="비밀번호 일치 테스트가 정상작동하지 않습니다.")

    def test_withdaw(self): # 회원탈퇴
        self.refresh = RefreshToken.for_user(self.user) # 토큰 refresh, access token 해킹방지용
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        # client = APIClient()
        # client.force_authenticate(user=self.user) # 강제 인증

        self.response = self.client.delete(self.withdraw_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT, msg="회원탈퇴 테스트가 정상 진행되지 않았습니다.")

    def test_withdaw_noself(self): # 회원 본인 아닌경우 탈퇴
        self.refresh = RefreshToken.for_user(self.user1) 
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')

        self.response = self.client.delete(self.withdraw_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN, msg="회원탈퇴는 권한있는 유저만 가능해야합니다.")
    # #--------결과값 확인 메서드-------------------
    # # 매 테스트 메소드 실행 후 동작
    # def tearDown(self):
    #     print(' 결과 값 : ',self.user.id)

# --------------토큰부분 미구현-----------------

    def test_token(self): # 토큰확인하기
        self.user_token_info = {
            "username" : 'testuser', 
            "password" : "kkkk1234",
        }

        self.response = self.client.post(self.token_url, data=self.user_token_info, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK, msg="토큰 테스트가 정상작동하지 않습니다.")

    def test_token_refresh(self): # 토큰 refresh 확인하기
        self.refresh = RefreshToken.for_user(self.user)
        self.user_token_info = {
            "refresh" : f"{self.refresh}", 
        }

        self.response = self.client.post(self.token_refresh_url, data=self.user_token_info, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK, msg="토큰 refresh 테스트가 정상작동하지 않습니다.")

    def test_token_verify(self): # 토큰 유효성검사 확인하기
        self.refresh = RefreshToken.for_user(self.user)
        user_token_info = {
                "token":f"{self.refresh.access_token}"
        }

        self.response = self.client.post(self.token_verify_ulr, data=user_token_info ,format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK, msg="토큰 verify 테스트가 정상작동하지 않습니다.")