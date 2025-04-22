import django_filters
from rest_framework.filters import OrderingFilter
from accounts.filters import UserFilter
from accounts.models import CustomUser
from accounts.serializers import ExportUserSerializer
from core.generic_base.base import BaseListAPIViewWithCSVExport


class ExportUserCSVView(BaseListAPIViewWithCSVExport):
    queryset = CustomUser.objects.select_related('role').all()
    filterset_class = UserFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name', 'email', 'is_staff', 'is_superuser', 'role__name']
    serializer_class = ExportUserSerializer
    export_csv_serializer_class = ExportUserSerializer
    csv_filename = 'users.csv'
    column_mapping = {
        0: 'name',
        1: 'email',
        2: 'is_staff',
        3: 'is_superuser',
        4: 'role__name'
    }