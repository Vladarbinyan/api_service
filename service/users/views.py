from rest_framework.pagination import LimitOffsetPagination
from users.models import User
from users.serializers import UserModelSerializer, UserModelSerializerSecond
from rest_framework import mixins, viewsets, generics
from rest_framework import permissions



# Create your views here.
class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 50


class UserMixinViews(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UsersLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerSecond
        return UserModelSerializer



