from django.db import models
from projects.models import Project

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    # Now many tasks can be assigned to one user
    assigned_to = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    
    status = models.CharField(
        max_length=50, 
        default='Todo', 
        choices=STATUS_CHOICES)
    
    priority = models.CharField(
        max_length=50, 
        default='Low', 
        choices=PRIORITY_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
