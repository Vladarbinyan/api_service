from users.models import User
from users.serializers import UserModelSerializer
from rest_framework import mixins, viewsets


# Create your views here.


class UserMixinViews(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
