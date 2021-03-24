from rest_framework.serializers import ModelSerializer
from todo_app.models import Project, Todo
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProjectSerializer(ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        exclude = ['uuid']


class TodoSerializer(ModelSerializer):
    project = ProjectSerializer()
    user = UserSerializer()

    class Meta:
        model = Todo
        fields = ['project', 'user', 'todo', 'text', 'is_active', 'create_date', 'update_date', ]

