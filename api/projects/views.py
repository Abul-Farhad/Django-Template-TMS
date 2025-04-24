from core.generic_base.base import BaseListAPIViewWithCSVExport
from projects.models import Project
from projects.serializers import ProjectSerializer
from projects.filters import ProjectFilter
from rest_framework.filters import OrderingFilter
import django_filters


class ProjectListAPIView(BaseListAPIViewWithCSVExport):
    queryset = Project.objects.prefetch_related('tasks').all()
    filterset_class = ProjectFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    serializer_class = ProjectSerializer
    export_csv_serializer_class = ProjectSerializer
    csv_filename = 'projects.csv'
    column_mapping = {
        0: 'title',
        1: 'description',
        2: 'priority',
        3: 'status',
        4: 'due_date',
    }
