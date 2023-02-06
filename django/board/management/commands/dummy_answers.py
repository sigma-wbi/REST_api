from django_seed import Seed
from django.core.management.base import BaseCommand
from random import *
from faker import Faker
from board.models import Question, Answer
from common.models import User

class Command(BaseCommand):

    help = 'This command creates answers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="How many answers do you want to create?"
        )

    def handle(self, *args, **options):
        fake = Faker()
        number = options.get('number')
        seeder = Seed.seeder()
        users = User.objects.all()
        questions = Question.objects.all()
        seeder.add_entity(Answer, number,{
            'author': lambda x: choice(users),
            'question': lambda x: choice(questions),
            'content': lambda x: fake.text(),
            'modify_date' : None
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} answers created!'))
