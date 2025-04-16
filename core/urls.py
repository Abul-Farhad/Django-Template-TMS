from django.urls import path
from .views import (
    DashboardView,
    ListUsersView
)

urlpatterns = [
    path('dashboard/',DashboardView.as_view(), name='dashboard'),
    path('users/', ListUsersView.as_view(), name='users'),
]