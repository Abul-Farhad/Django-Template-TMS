
from django.shortcuts import render
from django.views import View
from accounts.models import CustomUser
from accounts.forms import UserForm
from django.contrib import messages
from django.shortcuts import redirect


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
    
class UserCreateView(View):
    template_name = 'create_user.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash the password
            user.save()
            messages.success(request, "User created successfully.")
            return redirect('create_user')  # or wherever you want to redirect
        else:
            messages.error(request, "Please correct the errors below.")
        return render(request, self.template_name, {"form": form})

