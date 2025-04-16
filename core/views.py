from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from accounts.models import CustomUser

# def dashboard_view(request):
#     if request.user.is_authenticated:
#         return render(request, 'dashboard.html')
#     else:
#         messages.warning(request, 'You must be logged in to access this page.')
#         return redirect('login')  # Replace 'login' with your login URL name
    
class DashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            users_count = CustomUser.objects.count()  # Count the number of users
            return render(request, 'dashboard.html', {'users_count': users_count})
        else:
            messages.warning(request, 'You must be logged in to access this page.')
            return redirect('login')
        
class ListUsersView(View):
    def get(self, request):
        search_query = request.GET.get('q', '')  # Get the search query from the request
        if search_query:
            # Filter users by name (case-insensitive)
            users = CustomUser.objects.filter(name__icontains=search_query)
        else:
            # List all users if no search query is provided
            users = CustomUser.objects.all()
        return render(request, 'users.html', {'users': users})