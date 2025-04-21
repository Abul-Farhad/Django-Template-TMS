from django.urls import path
from .users.views import (
    ListUserAPIView,
)
from .csv.views import ExportUserCSVView
# from .permissions.views import(
#     PermissionListView
# )


urlpatterns = [
    path('user-list/', ListUserAPIView.as_view(), name='user-list'),
    path('export-user-csv/', ExportUserCSVView.as_view(), name='export-user-csv')
    # path('permission-list/', PermissionListView.as_view(), name='permission-list')

]