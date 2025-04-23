from django.urls import path

from api.tasks.views import TaskListAPIView
from .users.views import (
    ListUserAPIView,
)
from .csv.views import ExportTaskCSVView, ExportUserCSVView
from .role.views import RoleListSelectAPIView
# from .permissions.views import(
#     PermissionListView
# )


urlpatterns = [
    path('user-list/', ListUserAPIView.as_view(), name='user-list'),
    path('export-user-csv/', ListUserAPIView.as_view(), name='export-user-csv'),
    path('export-task-csv/', TaskListAPIView.as_view(), name='export-task-csv'),
    path('role-list/', RoleListSelectAPIView.as_view(), name='role-list'),
    # path('permission-list/', PermissionListView.as_view(), name='permission-list')
    path('task-list/', TaskListAPIView.as_view(), name='task-list'),

]