from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from random_username.generate import generate_username
import names


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        admin = kwargs['admin']
        for i in range(total):
            password = User.objects.make_random_password()
            if admin:
                user = User.objects.create_superuser(
                    username=generate_username()[0],
                    first_name=names.get_first_name(),
                    last_name=names.get_last_name(),
                    email='',
                    password=password,
                )
                print(f'Create new Superuser: {user} and password: {password}')
            else:
                user = User.objects.create_user(
                    username=generate_username()[0],
                    first_name=names.get_first_name(),
                    last_name=names.get_last_name(),
                    email='',
                    password=password,
                )
                print(f'Create new user: {user} and password: {password}')
