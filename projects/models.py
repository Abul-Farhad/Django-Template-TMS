from django.db import models

# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending',),
        ('Development', 'Development'), 
        ('Deployment', 'Deployment')
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('Pending', 'Pending'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=50, 
        default='Pending', 
        choices=STATUS_CHOICES)
    
    priority = models.CharField(
        max_length=50, 
        default='Low', 
        choices=PRIORITY_CHOICES)
    
    # task_list = models.ManyToManyField('tasks.Task', blank=True, null=True, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title