from django.urls import path
from .dashboard.views import DashboardView
from .users.views import ListUsersView


urlpatterns = [
    path('dashboard/',DashboardView.as_view(), name='dashboard'),   
    path('',DashboardView.as_view(), name='dashboard'),
    path('users/', ListUsersView.as_view(), name='users'),
    
    
    
]