import django_filters
from accounts.models import CustomUser  # Adjust this import to your structure

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    email = django_filters.CharFilter(field_name="email", lookup_expr='icontains')
    role = django_filters.CharFilter(field_name="role__name", lookup_expr='icontains')
    
    # Boolean filters
    is_staff = django_filters.BooleanFilter(field_name="is_staff")
    is_superuser = django_filters.BooleanFilter(field_name="is_superuser")

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'role', 'is_staff', 'is_superuser']
