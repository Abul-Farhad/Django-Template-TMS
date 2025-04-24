from core.generic_base.base import BaseListAPIViewWithCSVExport
from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.filters import TaskFilter
from rest_framework.filters import OrderingFilter
import django_filters
from django.core.paginator import Paginator
from rest_framework.response import Response

class TaskListAPIView(BaseListAPIViewWithCSVExport):
    """
    API view to retrieve a list of tasks.
    """
    # Define the queryset and serializer class
    queryset = Task.objects.select_related('assigned_to', 'project').all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter  # Define your filterset class if needed
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    csv_filename = 'tasks.csv'
    column_mapping = {
        0: 'title',
        1: 'description',
        2: 'assigned_to',
        3: 'project',
        4: 'priority',
        5: 'status',
        6: 'due_date',
    }

    # def stream_queryset_rows(self, queryset, writer):
    #     headers = list(self.column_mapping.values())
    #     yield writer.writerow(headers)

    #     print("Headers: ", headers)
    #     # Optional field-value custom render logic
    #     column_value_getters = {
    #         'assigned_to': lambda obj: getattr(obj.assigned_to, 'email', ''),
    #         'project': lambda obj: getattr(obj.project, 'title', ''),
    #     }

    #     for obj in queryset.iterator(chunk_size=1000):
    #         row = []
    #         for field in headers:
    #             if field in column_value_getters:
    #                 value = column_value_getters[field](obj)
    #             else:
    #                 value = getattr(obj, field, '')
    #             row.append(value)
    #         yield writer.writerow(row)


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search = self.request.GET.get('q')
    #     if search:
    #         queryset = queryset.filter(title__icontains=search)
    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     if request.GET.get('export') == 'csv':
    #         return super().list(request, *args, **kwargs)

    #     queryset = self.filter_queryset(self.get_queryset())
    #     page_number = int(request.GET.get("page", 1))
    #     paginator = Paginator(queryset, 5)
    #     page = paginator.get_page(page_number)
    #     print("Page Number: ", page_number)
    #     data = [{"id": task.id, "title": task.title} for task in page.object_list]
    #     return Response({
    #         "results": data,
    #         "pagination": {"more": page.has_next()},
            
    #     })

        