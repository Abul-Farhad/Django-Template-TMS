from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_staff', 'is_superuser', 'is_active', 'role')
    search_fields = ('email','name')
    list_filter = ('is_staff', 'is_active', 'role')


admin.site.register(CustomUser, CustomUserAdmin)