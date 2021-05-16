from django.core.management.base import BaseCommand
from todo_app.models import Project, Todo
from users.models import User
from mimesis import Internet, Text
import random


class Command(BaseCommand):
    help = 'Generate random data for Projects and TODO'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of todo to be created')

    def handle(self, *args, **kwargs):
        internet = Internet()
        text = Text()
        total = kwargs['total']
        for i in range(total):
            project = Project(title=text.title(), repository=internet.home_page(), text=text.words(quantity=5))
            project.save()
            random_user_list = []
            for _ in range(random.randint(1, 5)):
                random_user_list.append(str(random.choice(User.objects.values_list('uuid'))[0]))
            project.users.set(random_user_list)
            for _ in range(random.randint(1, 5)):
                todo = Todo(todo=text.title(),
                            text=text.text(quantity=2),
                            project=project,
                            user=User.objects.get(uuid=random.choice(User.objects.values_list('uuid'))[0]),
                            )
                todo.save()

