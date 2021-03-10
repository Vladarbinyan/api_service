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
            if admin:
                user = User(
                    username=person.username(),
                    first_name=person.first_name(),
                    last_name=person.last_name(),
                    email=person.email(),
                    is_superuser=True,
                )
                user.save()
                print(f'Create new Superuser: {user}')
            else:
                user = User(
                    username=person.username(),
                    first_name=person.first_name(),
                    last_name=person.last_name(),
                    email=person.email(),
                )
                user.save()
                print(f'Create new user: {user}')
