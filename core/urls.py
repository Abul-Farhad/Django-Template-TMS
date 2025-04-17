from django.urls import path
from .views import (
    DashboardView,
    ListUsersView,
    ExportUserCSVView,
    ExportUserEXELView
    
)

urlpatterns = [
    path('dashboard/',DashboardView.as_view(), name='dashboard'),
    path('users/', ListUsersView.as_view(), name='users'),
    path('export-users-csv/', ExportUserCSVView.as_view(), name='export-users-csv'),
    path('export-users-exel/', ExportUserEXELView.as_view(), name='export-users-excel' )
    
]