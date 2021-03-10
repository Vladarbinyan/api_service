from rest_framework.serializers import ModelSerializer
from todo_app.models import Project, Todo
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User


class ProjectSerializer(ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(ModelSerializer):
    projects = ProjectSerializer()
    users = UserSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
