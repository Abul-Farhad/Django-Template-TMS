import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    assigned_to = django_filters.CharFilter(field_name='assigned_to__email', lookup_expr='icontains')
    project = django_filters.CharFilter(field_name='project__title', lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=Task.STATUS_CHOICES)
    priority = django_filters.ChoiceFilter(choices=Task.PRIORITY_CHOICES)
    due_date = django_filters.DateFilter(lookup_expr='exact')

    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'project', 'status', 'priority', 'due_date']