from django.http import JsonResponse
from django.views import View
import django_filters
from accounts.filters import UserFilter
from accounts.models import CustomUser
from accounts.serializers import ExportUserSerializer
from core.generic_base.base import BaseListAPIViewWithCSVExport
from rest_framework.filters import OrderingFilter



# class ListUserAPIView(View):
#     def get(self, request):
#         draw = int(request.GET.get('draw', 1))
#         start = int(request.GET.get('start', 0))
#         length = int(request.GET.get('length', 10))

#         name = request.GET.get('name', '')
#         email = request.GET.get('email', '')
#         role = request.GET.get('role', '')

#         # Handle ordering
#         order_column_index = request.GET.get('order[0][column]', None)
#         order_dir = request.GET.get('order[0][dir]', 'asc')
#         columns = ['name', 'email', 'is_staff', 'is_superuser', 'role__name']
#         # print("Columns fields: ", columns)
#         order_column = columns[int(order_column_index)]
#         if order_dir == 'desc':
#             order_column = '-' + order_column
        
#         # print("Order Column: ", order_column)
#         # print("Order Column Index: ", order_column_index)

#         # Queryset
#         users = CustomUser.objects.select_related('role')

#         if name:
#             users = users.filter(name__icontains=name)
#         if email:
#             users = users.filter(email__icontains=email)
#         if role:
#             users = users.filter(role__name__icontains=role)

#         total_count = users.count()

#         # Apply ordering and pagination
#         users = users.order_by(order_column)[start:start+length]

#         data = [
#             {
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email,
#                 "is_staff": user.is_staff,
#                 "is_superuser": user.is_superuser,
#                 "role": user.role.name if user.role else None
#             }
#             for user in users
#         ]

#         return JsonResponse({
#             "draw": draw,
#             "recordsTotal": total_count,
#             "recordsFiltered": total_count,
#             "data": data
#         })
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
