from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'priority')
    search_fields = ('title',)
    list_filter = ('status', 'priority')

admin.site.register(Project, ProjectAdmin)