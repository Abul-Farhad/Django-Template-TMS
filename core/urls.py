from django.urls import path
from .dashboard.views import DashboardView
from .users.views import ListUsersView, UserCreateView


urlpatterns = [
    path('dashboard/',DashboardView.as_view(), name='dashboard'),   
    path('',DashboardView.as_view(), name='dashboard'),
    path('users/', ListUsersView.as_view(), name='users'),
    path('users/create/', UserCreateView.as_view(), name='user_create')
    
    
    
]