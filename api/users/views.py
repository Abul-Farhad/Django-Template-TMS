from django.http import JsonResponse
from django.views import View
from django.core import serializers
from accounts.models import CustomUser
import json


from django.views import View
from django.http import JsonResponse
from accounts.models import CustomUser

class ListUserAPIView(View):
    def get(self, request):
        search_query = request.GET.get('q', '')

        if search_query:
            users = CustomUser.objects.select_related('role').filter(name__icontains=search_query)
        else:
            users = CustomUser.objects.select_related('role').all()

        data = [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
                "role": user.role.name if user.role else None  # Safely handle null roles
            }
            for user in users
        ]
        return JsonResponse(data=data, safe=False)
