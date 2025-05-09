import django_filters
from .models import Role

class RoleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    class Meta:
        model = Role
        fields = ['name']
        
