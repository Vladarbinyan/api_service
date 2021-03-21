from rest_framework.pagination import LimitOffsetPagination
from users.models import User
from users.serializers import UserModelSerializer
from rest_framework import mixins, viewsets, generics
import logging

log = logging.getLogger('service_log')


# Create your views here.
class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class UserMixinViews(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # pagination_class = UsersLimitOffsetPagination



