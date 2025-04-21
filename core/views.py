# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.views import View
# from django.core import serializers
# from django.http import JsonResponse, StreamingHttpResponse
# from openpyxl import Workbook
# from accounts.models import CustomUser
# import csv
# from django.http import HttpResponse
# from openpyxl import Workbook
# from openpyxl.styles import Font, PatternFill
# # def dashboard_view(request):
# #     if request.user.is_authenticated:
# #         return render(request, 'dashboard.html')
# #     else:
# #         messages.warning(request, 'You must be logged in to access this page.')
# #         return redirect('login')  # Replace 'login' with your login URL name
    








# class ExportUserEXELView(View):
#     def get(self, request):
#         if not request.user.is_authenticated or not request.user.is_staff:
#             return HttpResponse(status=403)

#         # Create a new Excel workbook and active worksheet
#         wb = Workbook()
#         ws = wb.active
#         ws.title = "Users"

#         # Define styles
#         header_font = Font(size=12, bold=True)
#         odd_fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")  # light gray
#         even_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")  # white

#         # Add header row with styles
#         headers = ['Name', 'Email', 'Is Staff', 'Is Superuser', 'Role']
#         ws.append(headers)
#         for col_num, _ in enumerate(headers, 1):
#             cell = ws.cell(row=1, column=col_num)
#             cell.font = header_font

#         # Populate user data
#         users = CustomUser.objects.select_related('role').all()
#         for idx, user in enumerate(users, start=2):
#             row = [
#                 user.name,
#                 user.email,
#                 'Yes' if user.is_staff else 'No',
#                 'Yes' if user.is_superuser else 'No',
#                 user.role.name if user.role else '—'
#             ]
#             ws.append(row)

#             # Apply alternating row fill
#             fill = odd_fill if idx % 2 else even_fill
#             for col_num in range(1, len(row) + 1):
#                 ws.cell(row=idx, column=col_num).fill = fill

#         # Generate and return the Excel file as response
#         response = HttpResponse(
#             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         )
#         response['Content-Disposition'] = 'attachment; filename=users.xlsx'
#         wb.save(response)
#         return response


        