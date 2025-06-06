from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('auth/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('role/', include('permissions.urls'))
]