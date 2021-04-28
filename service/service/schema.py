import graphene
from graphene_django import DjangoObjectType
from todo_app.models import Project, Todo
from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        exclude = ['uuid']


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(TodoType)
    todo_by_uuid = graphene.Field(TodoType, uuid=graphene.String(required=True))
    todo_by_username = graphene.List(TodoType, username=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    def resolve_todo_by_uuid(self, info, uuid):
        try:
            return Todo.objects.get(uuid=uuid)
        except Todo.DoesNotExist:
            return None

    def resolve_todo_by_username(self, info, username=None):
        todo = Todo.objects.all()
        if username:
            todo = todo.filter(user__username=username)
        return todo


schema = graphene.Schema(query=Query)
