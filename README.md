# (가제목) DRF를 사용한 REST API

## 배포
REST API: http://cp2de.duckdns.org/api/common/  
API Document: https://cp2de.gitbook.io/rest_api-and-etl-pipeline/  

## 프로젝트 소개
DRF(Django REST Framework)를 사용하여 REST API를 만들고 배포

## API 주요 기능
1. 회원가입, 회원목록, API접근을 위한 jwt발급 등 회원정보 처리
2. 질문글과 답변글 CRRUD 기능(Create, Read, Retrieve, Update, Delete)
3. 회원들의 활동에 대한 통계
4. 회원들의 활동에 대한 Log 제공

## API 부가 기능
1. Django의 User Model은 상황에 맞게 커스터마이징
2. username과 password를 입력해 jwt 발급, jwt로 API사용
3. API에 대한 권한 설정
    - 사용자 목록, Log 등 중요한 정보는 staff 사용자만 접근 가능
    - 질문글 수정은 본인만 가능, 삭제는 본인과 staff만 가능
4. API로 받은 Log는 암호키가 있어야 복호화 가능
5. App을 내부적으로 테스트하는 기능

## Browsable API
웹브라우저로 접속 시 UI 사용  
웹브라우저가 아닌 다른 방식으로 사용하면 JSON형태로 반환
![image](https://user-images.githubusercontent.com/110042369/218315864-61809de1-5867-449c-8824-fd28a9b22881.png)

## 📚Stack
![badge](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white)
![badge](https://img.shields.io/badge/Django_REST_Framework-092E20?style=flat-square&logoColor=white)
![badge](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white)
![badge](https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white)
![badge](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white)  
![badge](https://img.shields.io/badge/AmazonEC2-FF9900?style=flat-square&logo=AmazonEC2&logoColor=white)
![badge](https://img.shields.io/badge/AmazonRDS-527FFF?style=flat-square&logo=AmazonRDS&logoColor=white)
![badge](https://img.shields.io/badge/AmazonS3-527FFF?style=flat-square&logo=AmazonS3&logoColor=white)
![badge](https://img.shields.io/badge/LetsEncrypt-003A70?style=flat-square&logo=LetsEncrypt&logoColor=white)

## Installation
파이썬 버전 : 3.9.16
데이터베이스 : MySQL
1. 레포지토리 클론
```python
$ git clone https://github.com/cp2-2team/cp2_api.git
```
2. 데이터 베이스 생성
```sql
mysql> CREATE DATABASE <DB이름> character set utf8mb4 collate utf8mb4_general_ci;
```
3. .env 파일 DB정보 설정
```python
DB_NAME='DB이름'
DB_USER='유저아이디'        #root
DB_PASSWORD='비밀번호'
```
4. 패키지 다운로드
```python
$ pip install -r requirements.txt
```

## Examples
API Document: https://cp2de.gitbook.io/rest_api-and-etl-pipeline/

## 추후 과제
- APACHE AIRFLOW를 사용해 ETL 파이프라인 만들기
- REACT로 프론트엔드를 만들고 API를 사용하여 웹페이지 만들기
