from django.urls import path
from .users.views import (
    ListUserAPIView,
)
# from .permissions.views import(
#     PermissionListView
# )


urlpatterns = [
    path('user-list/', ListUserAPIView.as_view(), name='user-list'),
    # path('permission-list/', PermissionListView.as_view(), name='permission-list')

]