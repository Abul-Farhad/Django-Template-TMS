from django.urls import path
from api.tasks.views import TaskListAPIView
from .users.views import ListUserAPIView
from .role.views import RoleListSelectAPIView
from .projects.views import ProjectListAPIView


urlpatterns = [
    path('user-list/', ListUserAPIView.as_view(), name='user-list'),
    path('export-user-csv/', ListUserAPIView.as_view(), name='export-user-csv'),
    path('export-task-csv/', TaskListAPIView.as_view(), name='export-task-csv'),
    path('role-list/', RoleListSelectAPIView.as_view(), name='role-list'),
    path('task-list/', TaskListAPIView.as_view(), name='task-list'),
    path('project-list/', ProjectListAPIView.as_view(), name='project-list'),

]