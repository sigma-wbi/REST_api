from django_seed import Seed
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from common.models import User
from random import *
from faker import Faker

#명령어 
#python manage.py dummy_users <--number 생성개수>

class Command(BaseCommand):

    help = 'This command creates users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="How many users do you want to create?"
        )

    def handle(self, *args, **options):
        fake = Faker()
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number,{
            # 람다 함수를 주어야 --number 옵션으로 여러개의 더미를 만들때 패스워드와 전화번호가 
            # 쌩 랜덤으로 생성된다 (아닐시 5개의 전화번호 생성하면 5개가 같은 전화번호로 생성)
            "password" : lambda x : make_password(fake.password()),
            'is_staff': False,
            "is_superuser": False,
            "last_login": None,
            "phone" :  lambda y : '010' + str(int(random() * 100000000))
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))