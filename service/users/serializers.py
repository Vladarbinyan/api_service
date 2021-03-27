from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import User
from .models import Author, Book
import logging

logger = logging.getLogger('service_log')


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def is_valid(self, raise_exception=False):
        ret = super(UserModelSerializer, self).is_valid(False)
        if self._errors:
            logger.warning("Serialization failed due to {}".format(self.errors))
            if raise_exception:
                raise ValidationError(self.errors)
        return ret


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializerBase(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'
