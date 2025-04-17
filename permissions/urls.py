from django.urls import path
from .views import (
    RoleCreateView,
    PermissionListView,
    RoleListView
)

urlpatterns = [
    path('role-create/', RoleCreateView.as_view(), name='role-create'),
    path('permission-list/', PermissionListView.as_view(), name='permission-list'),
    path('role-list/', RoleListView.as_view(), name='role-list')

]