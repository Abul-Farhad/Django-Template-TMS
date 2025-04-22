import django_filters
from permissions.models import Role
from permissions.serializers import RoleSerializer
from core.generic_base.base import BaseListAPIViewWithCSVExport
from django.core.paginator import Paginator
from rest_framework.response import Response

class RoleListSelectAPIView(BaseListAPIViewWithCSVExport):
    queryset = Role.objects.all().order_by("name")
    serializer_class = RoleSerializer  # Optional, only used for full DataTables
    export_csv_serializer_class = RoleSerializer  # If exporting CSV
    column_mapping = {
        0: 'name'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def list(self, request, *args, **kwargs):
        if request.GET.get('export') == 'csv':
            return super().list(request, *args, **kwargs)

        queryset = self.filter_queryset(self.get_queryset())
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(queryset, 3)
        page = paginator.get_page(page_number)

        data = [{"id": role.id, "name": role.name} for role in page.object_list]
        return Response({
            "results": data,
            "pagination": {"more": page.has_next()},
            
        })

