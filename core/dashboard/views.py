from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from accounts.models import CustomUser


class DashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            print("Yes, authenticated")
            users_count = CustomUser.objects.count()  # Count the number of users
            return render(request, 'dashboard.html', {'users_count': users_count})
        else:
            print("No, not authenticated")
            messages.warning(request, 'You must be logged in to access this page.')
            return redirect('login')
        