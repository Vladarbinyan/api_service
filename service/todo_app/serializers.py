from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from todo_app.models import Project, Todo
from users.models import User
import logging

logger = logging.getLogger('service_log')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProjectSerializer(ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        ret = super(ProjectSerializer, self).is_valid(False)
        if self._errors:
            logger.warning("Serialization failed due to {}".format(self.errors))
            if raise_exception:
                raise ValidationError(self.errors)
        return ret


class TodoSerializerBase(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['uuid', 'project', 'user', 'todo', 'text', 'is_active', 'create_date', 'update_date', ]


class TodoSerializer(ModelSerializer):
    project = ProjectSerializer()
    user = UserSerializer()

    class Meta:
        model = Todo
        fields = ['uuid', 'project', 'user', 'todo', 'text', 'is_active', 'create_date', 'update_date', ]

    def is_valid(self, raise_exception=False):
        ret = super(TodoSerializer, self).is_valid(False)
        if self._errors:
            logger.warning("Serialization failed due to {}".format(self.errors))
            if raise_exception:
                raise ValidationError(self.errors)
        return ret
