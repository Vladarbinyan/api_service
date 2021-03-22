# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from todo_app.serializers import ProjectSerializer, TodoSerializer
from todo_app.models import Project, Todo
from .filters import ProjectFilter, TodoFilter



class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination




class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = TodoFilter
    pagination_class = TodoLimitOffsetPagination
