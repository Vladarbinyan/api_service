from rest_framework.pagination import LimitOffsetPagination
from users.models import User
from users.serializers import UserModelSerializer
from rest_framework import mixins, viewsets, generics
from rest_framework import permissions
from .serializers import AuthorSerializer, BookSerializer, BookSerializerBase
from .models import Author, Book


# Create your views here.
class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class UserMixinViews(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, generics.GenericAPIView, mixins.CreateModelMixin):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # pagination_class = UsersLimitOffsetPagination


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BookSerializer
        return BookSerializerBase
