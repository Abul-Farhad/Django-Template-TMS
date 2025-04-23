from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'assigned_to', 'project', 'status', 'priority', 'created_at', 'updated_at', 'due_date')
    # search_fields = ('title',)
    list_filter = ('status', 'priority')
    autocomplete_fields = ['assigned_to', 'project']

admin.site.register(Task, TaskAdmin)

