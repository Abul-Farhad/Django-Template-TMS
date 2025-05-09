# import csv
# from django.http import HttpResponse, StreamingHttpResponse
# from django.views import View

# from accounts.models import CustomUser


# class Echo:
#     """A helper class to stream CSV rows as they're written."""
#     def write(self, value):
#         return value


# class ExportUserCSVView(View):
#     def get(self, request):
#         if not request.user.is_authenticated or not request.user.is_staff:
#             return HttpResponse(status=403)

#         # Define the streaming response

#         response = StreamingHttpResponse(
#             self.stream_users(request),
#             content_type='text/csv'
#         )
#         response['Content-Disposition'] = 'attachment; filename="users.csv"'
#         return response

#     def stream_users(self, request):

#         name = request.GET.get('name', '')
#         email = request.GET.get('email', '')
#         role = request.GET.get('role', '')

#         # Handle ordering
#         order_column_index = request.GET.get('order[0][column]', 0)
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
        
#         users = users.order_by(order_column)

#         """Generator that yields CSV lines."""
#         pseudo_buffer = Echo()
#         writer = csv.writer(pseudo_buffer)

#         # Write header first
#         yield writer.writerow(['Name', 'Email', 'Is Staff', 'Is Superuser', 'Role'])

#         # Stream results using iterator
#         queryset = users.iterator(chunk_size=1000)
#         for user in queryset:
#             yield writer.writerow([
#                 user.name,
#                 user.email,
#                 'Yes' if user.is_staff else 'No',
#                 'Yes' if user.is_superuser else 'No',
#                 user.role.name if user.role else '—'
#             ])



