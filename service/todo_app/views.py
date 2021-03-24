# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from todo_app.serializers import ProjectSerializer, TodoSerializer
from todo_app.serializers import Project, Todo


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
