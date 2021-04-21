from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import User

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



