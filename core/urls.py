from django.urls import path
from .dashboard.views import DashboardView
from .users.views import ListUsersView, UserCreateView
from .tasks.views import ListTasksView, CreateTaskView


urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard'),
    path('dashboard/',DashboardView.as_view(), name='dashboard'),   
    path('users/', ListUsersView.as_view(), name='users'),
    path('users/create/', UserCreateView.as_view(), name='create_user'),
    path('tasks/', ListTasksView.as_view(), name='tasks'),
    path('tasks/create/', CreateTaskView.as_view(), name='create_task'),    
]