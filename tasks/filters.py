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

    # Custom filter for tasks with no project
    task_assigned_to_project = django_filters.BooleanFilter(
        method='filter_task_by_assignment_status_for_project',
        label='Filter tasks with no project'
    )


    def filter_task_by_assignment_status_for_project(self, queryset, name, value):
        if not value:  # If the filter is set to unassigned
            print("Filtering tasks with no project", value)
            return queryset.filter(project__isnull=True)
        print("Filtering tasks with project", value)
        return queryset.filter(project__isnull=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'project', 'status', 'priority', 'due_date', 'task_assigned_to_project']