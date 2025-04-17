from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_staff', 'is_superuser', 'is_active', 'role')
    search_fields = ('username', 'email', 'role')
    list_filter = ('is_staff', 'is_active', 'role')

    # def assigned_projects(self, obj):
    #     return ", ".join([project.name for project in obj.projects.all()])
    # assigned_projects.short_description = 'Assigned Projects'

admin.site.register(CustomUser, CustomUserAdmin)