
from django.shortcuts import render
from django.views import View
from accounts.models import CustomUser


class ListUsersView(View):
    def get(self, request):
        # search_query = request.GET.get('q', '')  # Get the search query from the request
        # if search_query:
        #     # Filter users by name (case-insensitive)
        #     users = CustomUser.objects.filter(name__icontains=search_query).order_by('id')
        # else:
        #     # List all users if no search query is provided
        #     users = CustomUser.objects.all().order_by('id')
        # return render(request, 'users.html', {'users': users})
        return render(request, 'users.html', {})
