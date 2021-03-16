from django_filters import rest_framework as filters
from .models import Project, Todo


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = [
            'title',
        ]


class TodoFilter(filters.FilterSet):
    project = filters.ModelChoiceFilter(queryset=Project.objects.all())
    create_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Todo
        fields = [
            'project',
            'create_date',
        ]
