import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=Project.STATUS_CHOICES)
    priority = django_filters.ChoiceFilter(choices=Project.PRIORITY_CHOICES)
    due_date = django_filters.DateFilter(lookup_expr='exact')
    created_at = django_filters.DateTimeFromToRangeFilter()
    updated_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'status', 'priority', 'created_at', 'updated_at']