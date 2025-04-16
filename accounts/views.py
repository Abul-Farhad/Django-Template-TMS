from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from django.views import View
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Replace 'home' with your desired redirect URL name
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):    
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL name
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Please correct the errors below.')


    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Replace 'login' with your login URL name
    
    return render(request, 'logout.html', {})

class LogoutView(View):
        
    def post(self, request):
        logout(request)
        return redirect('login')  # Replace 'login' with your login URL name


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Replace 'login' with your login URL name
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Replace 'login' with your login URL name
        else:
            messages.error(request, 'Please correct the errors below.')
        
        return render(request, 'register.html', {'form': form})




