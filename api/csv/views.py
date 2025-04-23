import django_filters
from rest_framework.filters import OrderingFilter
from accounts.filters import UserFilter
from accounts.models import CustomUser
from accounts.serializers import ExportUserSerializer
from core.generic_base.base import BaseListAPIViewWithCSVExport
from tasks.filters import TaskFilter
from tasks.models import Task
from tasks.serializers import TaskSerializer


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


class ExportTaskCSVView(BaseListAPIViewWithCSVExport):
    queryset = Task.objects.select_related('assigned_to', 'project').all()
    filterset_class = TaskFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    serializer_class = TaskSerializer
    export_csv_serializer_class = TaskSerializer
    csv_filename = 'tasks.csv'
    column_mapping = {
        0: 'title',
        1: 'description',
        2: 'assigned_to__email',
        3: 'project__title',
        4: 'priority',
        5: 'status',
        6: 'due_date',
    }