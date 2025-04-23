import django_filters
from rest_framework import serializers
from rest_framework.filters import OrderingFilter
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.CharField(source='assigned_to.email', default='—')
    project = serializers.CharField(source='project.title', default='—')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'project', 'status', 'priority', 'due_date']
        read_only_fields = ['created_at', 'updated_at']