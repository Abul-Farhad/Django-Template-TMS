from django.http import JsonResponse
from django.views import View
import django_filters
from accounts.filters import UserFilter
from accounts.models import CustomUser
from accounts.serializers import ExportUserSerializer
from core.generic_base.base import BaseListAPIViewWithCSVExport
from rest_framework.filters import OrderingFilter
from django.core.paginator import Paginator
from rest_framework.response import Response


class ListUserAPIView(BaseListAPIViewWithCSVExport):
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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search = self.request.GET.get('q')
    #     if search:
    #         queryset = queryset.filter(email__icontains=search)
    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     if request.GET.get('export') == 'csv':
    #         return super().list(request, *args, **kwargs)

    #     queryset = self.filter_queryset(self.get_queryset())
    #     page_number = int(request.GET.get("page", 1))
    #     paginator = Paginator(queryset, 5)
    #     page = paginator.get_page(page_number)
    #     print("Page Number: ", page_number)
    #     data = [{"id": user.id, "email": user.email} for user in page.object_list]
    #     return Response({
    #         "results": data,
    #         "pagination": {"more": page.has_next()},
            
    #     })
