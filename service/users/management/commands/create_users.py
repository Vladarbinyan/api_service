from users.models import User
from django.core.management.base import BaseCommand
from mimesis import Person


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        person = Person('ru')
        total = kwargs['total']
        admin = kwargs['admin']
        for i in range(total):
            password = User.objects.make_random_password()
            if admin:
                user = User.objects.create_superuser(
                    username=person.username(),
                    first_name=person.first_name(),
                    last_name=person.last_name(),
                    email=person.email(),
                    password=password,
                )
                print(f'Create new Superuser: {user} and password: {password}')
            else:
                user = User.objects.create_user(
                    username=person.username(),
                    first_name=person.first_name(),
                    last_name=person.last_name(),
                    email=person.email(),
                    password=password,
                )
                print(f'Create new user: {user} and password: {password}')
