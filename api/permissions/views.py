# # permissions/views.py
# import json
# from django.http import JsonResponse
# from django.views import View
# from django.shortcuts import get_object_or_404
# from accounts.models import CustomUser
# from permissions.forms import RoleForm
# from permissions.models import Role, Permission

# # from asgiref.sync import sync_to_async


# class RoleListView(View):
#     def get(self, request):
#         roles = Role.objects.prefetch_related('permissions').all()  # Optimize query with prefetch_related
#         role_list = [
#             {
#                 'id': role.id,
#                 'name': role.name,
#                 'permissions': list(role.permissions.values('id', 'name', 'codename'))
#             }
#             for role in roles
#         ]
#         return JsonResponse(role_list, safe=False)

# class RoleCreateView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         form = RoleForm(data)
#         if form.is_valid():
#             role = form.save()
#             return JsonResponse({
#                 'id': role.id,
#                 'name': role.name,
#                 'permissions': list(role.permissions.values('id', 'name', 'codename'))
#             }, status=201)
#         return JsonResponse({'errors': form.errors}, status=400)


# class RoleDetailView(View):
#     def get(self, request, role_id):
#         role = get_object_or_404(Role, id=role_id)
#         return JsonResponse({
#             'id': role.id,
#             'name': role.name,
#             'permissions': list(role.permissions.values('id', 'name', 'codename'))
#         })
        
# class RoleUpdateView(View):
#     def put(self, request, role_id):
#         role = get_object_or_404(Role, id=role_id)
#         data = json.loads(request.body)
#         form = RoleForm(data, instance=role)
#         if form.is_valid():
#             updated_role = form.save()
#             return JsonResponse({
#                 'id': updated_role.id,
#                 'name': updated_role.name,
#                 'permissions': list(updated_role.permissions.values('id', 'name', 'codename'))
#             })
#         return JsonResponse({'errors': form.errors}, status=400)

# class RoleDeleteView(View):
#     def delete(self, request, role_id):
#         role = get_object_or_404(Role, id=role_id)
#         role.delete()
#         return JsonResponse({'message': 'Role deleted successfully'}, status=204)

# class PermissionListView(View):
#     def get(self, request):
#         permissions = Permission.objects.all().values('id', 'name', 'codename')
#         return JsonResponse(list(permissions), safe=False)
    
# class AssignRoleToUserView(View):
#     def post(self, request):
#         try:
#             print("YOO##########################3")
#             # Parse the JSON body
#             data = json.loads(request.body)
#             print(data)
#             user_id = data.get('user_id')
#             role_id = data.get('role_id')

#             # Validate input
#             if not user_id or not role_id:
#                 return JsonResponse({'error': 'user_id and role_id are required.'}, status=400)

#             # Get the user and role objects
#             user = get_object_or_404(CustomUser, id=user_id)
#             role = get_object_or_404(Role, id=role_id)
            
#             # Assign the role to the user
#             user.role = role
#             user.save()

#             return JsonResponse({'message': f"Role '{role.name}' assigned to user '{user.name}' successfully."}, status=200)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)